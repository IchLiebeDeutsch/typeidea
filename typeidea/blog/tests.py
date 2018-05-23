# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pprint import pprint as pp

from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase
from django.test.utils import override_settings

from .models import Category
from .models import Post
# Create your tests here.


class TestCategory(TestCase):

    @override_settings(DEBUG=True)
    def setUp(self):
        self.user = user = User.objects.create_user(username='the5fire', email='the5fire@gmail.com', password='password')
        Category.objects.bulk_create([
            Category(name='cate_bulk_%s' % i, owner=user)
            for i in range(10)
        ])

    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.filter(status=1).select_related('owner').defer('owner__username')
        for cate in categories:
            print(cate.owner.first_name)
        pp(connection.queries)

    def test_value(self):
        categories = Category.objects.values('name')
        pp(categories)