# coding:utf-8

from __future__ import unicode_literals

from django.contrib.admin.sites import AdminSite


class CustomSite(AdminSite):
    site_header = 'typeidea管理'
    site_title = 'typeidea'
    index_title = '首页'


custom_site = CustomSite('cus_site')