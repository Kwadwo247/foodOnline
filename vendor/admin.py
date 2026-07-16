from django.contrib import admin
from .models import Vendor
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name','user','user_profile','is_approved','created_at')
    list_display_links = ('user','vendor_name')

admin.site.register(Vendor, VendorAdmin)