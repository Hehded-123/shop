from django.contrib import admin
from .models import Product,ContactUs


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','price','created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content','price','created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(ContactUs)