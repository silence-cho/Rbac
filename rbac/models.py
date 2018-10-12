from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    age = models.IntegerField()
    role = models.ForeignKey(to='Role')
    def __str__(self):
        return self.name

class Role(models.Model):
    title = models.CharField(max_length=32)
    permission = models.ManyToManyField(to='Permission')

    def __str__(self):
        return self.title

class Permission(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    action = models.CharField(max_length=32)
    group = models.ForeignKey(to='PermissionGroup')
    def __str__(self):
        return self.title

class PermissionGroup(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title


