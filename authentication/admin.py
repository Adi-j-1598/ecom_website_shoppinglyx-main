from django.contrib import admin

from authentication.models import CustomUser

class CustomUserModelAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','is_seller','is_buyer']
admin.site.register(CustomUser,CustomUserModelAdmin)
