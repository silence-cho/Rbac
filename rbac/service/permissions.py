#coding:utf-8

from rbac import models

def initial_permission(request,user):

    permissions = models.Role.objects.filter(user=user).values('permission__url','permission__action','permission__group_id').distinct()
    permission_list = {}
    for item in permissions:
        if item['permission__group_id'] not in permission_list:
            permission_list[item['permission__group_id']]= {'permission__url':[item['permission__url'],],'permission__action':[item['permission__action'],]}
        else:
            permission_list[item['permission__group_id']]['permission__url'].append(item['permission__url'])
            permission_list[item['permission__group_id']]['permission__action'].append(item['permission__action'])
    #print permission_list
    request.session['permission_list'] = permission_list

    # 按用户组权限id分组，得到如下的数据结构，即对两张表分别的操作权限
    # {1: {'permission__url': [u'/user/', u'/user/edit/(\\d+)', u'/user/add/'],
    #      'permission__action': [u'list', u'edit', u'add']},
    #  2: {'permission__url': [u'/role/'], 'permission__action': [u'list']}}


    #设置菜单的显示权限数据
    menu_permissions = models.Role.objects.filter(user=user).values('permission__url','permission__action','permission__group__title').distinct()
    menu_permission_list=[]
    for item in menu_permissions:
        if item['permission__action'] == 'list':
            menu_permission_list.append((item['permission__url'],item['permission__group__title']))
    request.session['menu_permission_list'] = menu_permission_list
    # print menu_permission_list
