from django.contrib import admin

from inventory.models import Product, IOHistory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'available_quantity',]


class IOHistoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_in', 'quantity_out', 'date',]


admin.site.register(Product, ProductAdmin)
admin.site.register(IOHistory, IOHistoryAdmin)
