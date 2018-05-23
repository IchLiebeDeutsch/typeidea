# coding: utf-8
from __future__ import unicode_literals

from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(required=False, label='是否删除') #TODO:处理布尔类型为我们需要的字段
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)

    def clean_status(self):
        if self.cleaned_data['status']:
            return 3
        else:
            return 1

