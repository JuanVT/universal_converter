from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from control.models import Currency


@admin.register(Currency)
class CurrencyImportAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'code']
