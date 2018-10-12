#coding:utf-8

from django import template

register = template.Library()

@register.inclusion_tag('rbac/left_menu.html')
def get_menu(request):

    menu_permission_list = request.session.get('menu_permission_list')
    return {'menu_permission_list':menu_permission_list}
