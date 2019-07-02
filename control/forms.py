from django import forms

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
                  ("tablespoon", "Tablespoons"),
                  ("pint", "Pints"),
                  ("teaspoon", "Teaspoons"),
                  ("cubic inches", "Cubic Inches"),
                  ("milliliter", "ml"),
                  ("cubic centimeter", "Cubic Centimeters"),
                  ("cubic meter", "Cubic Meter")]


class VolumeConverter(forms.Form):

    unit = forms.ChoiceField(label='Unit', choices=volume_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=volume_choices)
    unit_value = forms.FloatField(initial=0)
