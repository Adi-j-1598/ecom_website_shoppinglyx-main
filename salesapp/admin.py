from django.contrib import admin
from salesapp.models import Seller

@admin.register(Seller)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','seller_name','locality','city','zipcode','state']



