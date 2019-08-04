from django.contrib import admin

from control.models import Currency


@admin.register(Currency)
class ConverterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']
