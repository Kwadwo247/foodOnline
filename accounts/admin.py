from django.contrib import admin
from . import models
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','first_name','last_name','role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.UserProfile)