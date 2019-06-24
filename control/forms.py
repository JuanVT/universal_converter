from django.forms import ModelForm

from control.models import Converter


class ConverterForm(ModelForm):
    class Meta:
        model = Converter
        fields = ['unit', 'unit_to', 'unit_value']
