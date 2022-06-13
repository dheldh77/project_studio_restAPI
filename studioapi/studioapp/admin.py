from django.contrib import admin
from .models import MerchantInfo, Category, MerchantLocation, Photo, ExternalUrl

# Register your models here.

admin.site.register(MerchantInfo)
admin.site.register(Category)
admin.site.register(MerchantLocation)
admin.site.register(Photo)
admin.site.register(ExternalUrl)
