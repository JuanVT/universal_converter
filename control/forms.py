from django import forms


# from control.models import Converter
#
#
# class ConverterForm(ModelForm):
#
#     class Meta:
#         model = Converter
#         fields = ['unit', 'unit_value', 'unit_to', ]
from django.utils.regex_helper import Choice

unit_choices = [("metre", "Metre"),
                ("kilometre", "Kilometre"),
                ("centimetre", "Centimetre"),
                ("millimetre", "Millimetre"),
                ("micrometre", "Micrometre"),
                ("nanometre", "Nanometre"),
                ("mile", "Mile"),
                ("yard", "Yard"),
                ("foot", "Foot"),
                ("inch", "Inch")]


class ConverterForm(forms.Form):

    unit = forms.ChoiceField(label='Unit', choices='unit_choices', initial='', widget=forms.Select(), required=True)
    unit_to = forms.ChoiceField(label='Unit to', choices='unit_choices', initial='', widget=forms.Select(), required=True)
    unit_value = forms.FloatField()
