"""
Based on:
http://www.tryolabs.com/Blog/2012/06/18/django-administration-interface-non-staff-users/
"""
from django.contrib.admin.sites import AdminSite


class UserAdmin(AdminSite):
    def has_permission(self, request):
        return request.user.is_active


user_admin_site = UserAdmin(name='crud')
