from django.contrib import admin

# Register your models here.


import models
from django.contrib.admin import ModelAdmin

class UserConfigure(ModelAdmin):
    list_display = ['name','role']

admin.site.register(models.User,admin_class=UserConfigure)
admin.site.register(models.Role)
admin.site.register(models.Permission)
admin.site.register(models.PermissionGroup)
