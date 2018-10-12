#coding:utf-8

#rbac：role-based access control 基于角色的权限控制

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
import re
#自定义中间件
class ValidPermission(MiddlewareMixin):

    def process_request(self,request):

        current_path = request.path  # 拿到当前请求路径  '/user/'

        #设置白名单，允许任何人访问的url
        valid_urls = ['/login/','/admin/(.*)']
        for url in valid_urls:
            path = '^%s$'%url
            ret = re.match(path, current_path)
            if ret:
                return None

        #对于没有登陆的用户重定向至登陆页面
        user_id = request.session.get('user',[])
        if not user_id:
            return redirect('/login/')

        #根据权限来匹配url，决定当前用户是否有访问权限
        permission_list = request.session['permission_list']
        # print permission_list,current_path
        for permission in permission_list.values():
            urls = permission['permission__url']
            for url in urls:
                path = '^%s$'%url
                ret = re.match(path,current_path)
                if ret:
                    request.actions = permission['permission__action']   #[u'list', u'edit', u'add']
                    # print request.actions
                    return None

        return HttpResponse('没有访问权限')