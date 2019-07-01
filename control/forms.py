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

length_choices = [("metre", "Metre"),
                  ("kilometre", "Kilometre"),
                  ("centimetre", "Centimetre"),
                  ("millimetre", "Millimetre"),
                  ("micrometre", "Micrometre"),
                  ("nanometre", "Nanometre"),
                  ("mile", "Mile"),
                  ("yard", "Yard"),
                  ("foot", "Foot"),
                  ("inch", "Inch")]


class LengthConverter(forms.Form):

    unit = forms.ChoiceField(label='Unit', choices=length_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=length_choices)
    unit_value = forms.FloatField(initial=0)


volume_choices = [("gallon", "Gallons"),
                  ("quart", "Quarts"),
                  ("ounce", "Ounces"),
                  ("litre", "Litres"),
                  ("tablespoon", "Tablespoon"),
                  ("teaspoon", "Teaspoon"),
                  ("cubic inches", "Cubic Inches"),
                  ("milliliter", "milliliters"),
                  ("cubic centimeter", "Cubic Centimeters"),
                  ("cubic meter", "Cubic Meter")]


class VolumeConverter(forms.Form):

    unit = forms.ChoiceField(label='Unit', choices=volume_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=volume_choices)
    unit_value = forms.FloatField(initial=0)
