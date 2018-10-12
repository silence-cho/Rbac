#coding:utf-8
from django.shortcuts import render,redirect
import models
from forms import UserForm,RoleForm

# Create your views here.

class PermissionAction(object):
    def __init__(self,actions):
        self.actions = actions

    def add_check(self):
        return 'add' in self.actions

    def edit_check(self):
        return 'edit' in self.actions

    def delete_check(self):
        return 'delete' in self.actions

def listUser(request):

    users = models.User.objects.all()
    user_id = request.session.get('user')
    user = models.User.objects.filter(id=user_id).first()
    permission_action = PermissionAction(request.actions)
    return render(request, 'rbac/listUser.html', locals())

def editUser(request,id):

    user_obj = models.User.objects.filter(id=id).first()
    form = UserForm(instance=user_obj)
    if request.method=='POST':
        form = UserForm(request.POST,instance=user_obj)
        form.save()
        return redirect('/user/')
    return render(request, 'rbac/edit.html',locals())   #首先在根目录下templates下找对应的html，若未找到在按app注册顺序找各app下的templates文件

def deleteUser(request,id):
    user_obj = models.User.objects.filter(id=id).first()
    result = {'url': 'user', 'data': user_obj.name,'id':id}
    if request.method=='POST':
        ret = models.User.objects.filter(id=id).delete()
        # print ret
        return redirect('/user/')
    return render(request, 'rbac/delete.html',locals())

def addUser(request):
    form = UserForm()
    if request.method=='POST':
        form = UserForm(request.POST)
        form.save()
        return redirect('/user/')
    return render(request, 'rbac/add.html',locals())


def listRole(request):
    roles = models.Role.objects.all()
    user_id = request.session.get('user')
    user = models.User.objects.filter(id=user_id).first()
    permission_action = PermissionAction(request.actions)
    return render(request, 'rbac/listRole.html', locals())

def editRole(request, id):
    role_obj = models.Role.objects.filter(id=id).first()
    form = RoleForm(instance=role_obj)
    if request.method == 'POST':
        form = RoleForm(request.POST,instance=role_obj)
        form.save()
        return redirect('/role/')
    return render(request, 'rbac/edit.html', locals())

def deleteRole(request, id):

    role_obj = models.Role.objects.filter(id=id).first()
    result = {'url': 'role', 'data':role_obj.title,'id':id}
    if request.method == 'POST':
        models.Role.objects.filter(id=id).delete()
        return redirect('/role/')
    return render(request, 'rbac/delete.html', locals())

def addRole(request):
    form = RoleForm()
    if request.method == 'POST':
        form = RoleForm(request.POST)
        form.save()
        return redirect('/role/')
    return render(request, 'rbac/add.html', locals())
