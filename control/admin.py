from django.contrib import admin

from control.models import Converter


@admin.register(Converter)
class ConverterAdmin(admin.ModelAdmin):

    list_display = ['id', 'unit', 'unit_to']
