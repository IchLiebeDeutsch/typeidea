# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category, Tag
from typeidea.custom_site import custom_site
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from .adminforms import PostAdminForm
from typeidea.custom_admin import BaseOwnerAdmin
# Register your models here.


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    list_display_links = ['category', 'status']
    search_fields = ['title', 'category__name', 'owner__first_name']
    save_on_top = False
    show_full_result_count = False  # 优化显示结果
    list_filter = ['title']

    actions_on_top = True
    date_hierarchy = 'created_time'
    list_editable = ['title', ]

    # 编辑页面
    fieldsets = (  # 跟fields互斥
        ('基础配置', {
            'fields': (('category', 'title'),
                       'desc',
                       'status',
                       'content')
        }),
        ('高级配置', {
            'classes': ('collapse', 'addon'),
            'fields': ('tag',),
        }),
    )  # 布局作用
    filter_horizontal = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_site:blog_post_change', args=(obj.id,))
        )
    operator.show_description = '操作'
    operator.empty_value_display = '???'


class PostInlineAdmin(admin.TabularInline):
    fields = ('title', 'status')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status','is_nav', 'created_time']
    inlines = [PostInlineAdmin,]
    fields = ('name', 'status', 'is_nav',)


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']

