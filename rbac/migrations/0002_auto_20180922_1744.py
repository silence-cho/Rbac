# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-22 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Uesr',
            new_name='User',
        ),
    ]
