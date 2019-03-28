#coding:utf-8



from django.conf.urls import url
import views
urlpatterns = [

    url(r'^login/$', views.login),
    url(r'^user/$', views.listUser),
    url(r'^user/add/', views.addUser),
    url(r'^user/edit/(\d+)', views.editUser),
    url(r'^user/delete/(\d+)', views.deleteUser),
    url(r'^role/$', views.listRole),
    url(r'^role/add/', views.addRole),
    url(r'^role/edit/(\d+)', views.editRole),
    url(r'^role/delete/(\d+)', views.deleteRole),

]