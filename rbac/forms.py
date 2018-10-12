#coding:utf-8

from django import forms
import models
class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        labels = {
            'name':'姓名',
            'password':'密码',
            'age':'年龄',
            "role":'角色'
        }
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'password': forms.widgets.TextInput(attrs={'class':'form-control','type':'password'}),
            'age': forms.widgets.TextInput(attrs={'class':'form-control','type':'number'}) ,
            "role": forms.widgets.Select(attrs={'class':'form-control'})
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = '__all__'
        labels = {
            'title': '角色',
            'permission': '权限'
        }
        widgets = {
            'title': forms.widgets.TextInput(attrs={'class':'form-control'}),
            'permission':  forms.widgets.SelectMultiple(attrs={'class':'form-control'})
        }