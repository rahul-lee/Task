from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from orderapp import models
admin.site.register(models.Product)
admin.site.register(models.Order)


class OrderAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'price')
