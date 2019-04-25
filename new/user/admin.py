from django.contrib import admin
from .models import Myuser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

@admin.register(Myuser)
class MyUserAdmin(UserAdmin):
    list_display = ['username','email','mobile']
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1]=(_('personal info'),{'fields':('first_name','last_name','email','mobile')})