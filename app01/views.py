#coding:utf-8
from django.shortcuts import render,redirect
# Create your views here.
from rbac import models
from rbac.service.permissions import initial_permission

def login(request):
    if request.method=='POST':
        name = request.POST.get('name')
        passsword = request.POST.get('password')
        # print name, passsword
        user_obj = models.User.objects.filter(name=name,password=passsword).first()
        if user_obj:
            request.session['user']=user_obj.pk
            initial_permission(request,user_obj)
            return redirect('/user/')
        else:
            return render(request,'login.html')
    return render(request, 'login.html')

