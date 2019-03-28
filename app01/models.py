#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=16,null=False)
    phone = models.CharField(verbose_name="手机",max_length=16)
    department = models.CharField(verbose_name="部门",max_length=16)
    salary = models.DecimalField(verbose_name="薪水",max_digits=7,decimal_places=2)

    class Meta:
        verbose_name = '姓名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
