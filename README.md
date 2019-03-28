# Rbac
Role-based access control（基于角色的权限控制系统）

role-based access control（rbac）：指对于不同角色的用户，拥有不同的权限 。

每个用户对应一个角色，一个角色拥有若干权限，形成用户-角色-权限的关系，当一个用户进行访问数据时，根据其角色判断其拥有的权限，限定其操作。

#使用指南
  1. 配置Rbac app
      将 Rbac app（整个Rbac文件夹）拷贝到自己的项目，在项目settings.py文件中注册app，然后进行数据库migrate,如下：
          
          #settings.py
          INSTALLED_APPS = [
             'myAdmin.apps.MyadminConfig', ]
          #控制台
          python manage.py makemigrations
          python manage.py migrate
  2. 添加权限控制
      登陆admin后台管理，为自己的数据添加权限（增删改查四条url），然后将权限赋予到不同角色。 如我的app01下面有一个Employee model,对应四个权限设置如下：
      
          查看职员     /app01/employee/
          添加职员    /app01/employee/add/
          编辑职员    /app01/employee/edit/(\d+)
          删除职员     /app01/employee/delete/(\d+)  
  
  3. 实现自己的增删改查函数
      对于上述Employee的四个url，对其路由进行配置，然后实现对应的处理函数即可。
  
  实现效果即简单过程参考：https://www.cnblogs.com/silence-cho/p/9781237.html

