from django.contrib import admin
from .models import *


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(CategoryModel,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','available','stock','updated']
    list_editable = ['price','available','stock']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(ProductModel,ProductAdmin)


admin.site.register(CartListModel)
admin.site.register(CartItemModel)