from django import forms

from control.models import Currency

LENGTH_CHOICES = [
    ('', 'Select..'),
    ("metre", "Metre"),
    ("kilometre", "Kilometre"),
    ("centimetre", "Centimetre"),
    ("millimetre", "Millimetre"),
    ("micrometre", "Micrometre"),
    ("nanometre", "Nanometre"),
    ("mile", "Mile"),
    ("yard", "Yard"),
    ("inch", "Inch"),
    ("foot", "Foot"),
]


class LengthConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=LENGTH_CHOICES)
    unit_to = forms.ChoiceField(label='Unit to', choices=LENGTH_CHOICES)
    unit_value = forms.FloatField(initial=0)


VOLUME_CHOICES = [
    ('', 'Select..'),
    ("gallon", "Gallons"),
    ("quart", "Quarts"),
    ("ounce", "Ounces"),
    ("litre", "Litres"),
    ("tablespoon", "Tablespoons"),
    ("pint", "Pints"),
    ("teaspoon", "Teaspoons"),
    ("cubic inches", "Cubic Inches"),
    ("milliliter", "ml"),
    ("cubic centimeter", "Cubic Centimeters"),
    ("cubic meter", "Cubic Meter")
]


class VolumeConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=VOLUME_CHOICES)
    unit_to = forms.ChoiceField(label='Unit to', choices=VOLUME_CHOICES)
    unit_value = forms.FloatField(initial=0)


TIME_CHOICES = [
    ('', 'Select..'),
    ('nanosecond', 'Nanosecond'),
    ('microsecond', 'Microsecond'),
    ('millisecond', 'Millisecond'),
    ('second', 'Second'),
    ('minute', 'Minute'),
    ('hour', 'Hour'),
    ('day', 'Day'),
    ('week', 'Week'),
    ('month', 'Month'),
    ('year', 'Year'),
    ('decade', 'Decade'),
    ('century', 'Century')
]


class TimeConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=TIME_CHOICES)
    unit_to = forms.ChoiceField(label='Unit to', choices=TIME_CHOICES)
    unit_value = forms.FloatField(initial=0)


class CurrencyConverter(forms.Form):
    currencies = Currency.objects.all()
    currency_choices = [('', 'Select..')] + [(currency.code, currency.name) for currency in currencies]

    unit = forms.ChoiceField(label='Unit', choices=currency_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=currency_choices)
    unit_value = forms.FloatField(initial=0)


TEMPERATURE_CHOICES = [
    ('', 'Select..'),
    ('celsius', 'Celsius'),
    ('kelvin', 'Kelvin'),
    ('fahrenheit', 'Fahrenheit')
]


class TemperatureConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=TEMPERATURE_CHOICES)
    unit_to = forms.ChoiceField(label='Unit to', choices=TEMPERATURE_CHOICES)
    unit_value = forms.FloatField(initial=0)


WEIGHT_CHOICES = [
    ('', 'Select..'),
    ('tonne', 'Tonne'),
    ('kg', 'Kilograms'),
    ('g', 'grams'),
    ('mg', 'Milligram'),
    ('micro gram', 'Micro gram'),
    ('imperial ton', 'Imperial Ton'),
    ('us ton', 'US Ton'),
    ('stone', 'Stone'),
    ('pound', 'Pound'),
    ('ounce', 'Ounce'),
]


class WeightConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=WEIGHT_CHOICES)
    unit_to = forms.ChoiceField(label='Unit to', choices=WEIGHT_CHOICES)
    unit_value = forms.FloatField(initial=0)


SPEED_CHOICES = [
    ('', 'Select..'),
    ('Miles per hour', 'Miles per hour'),
    ('metre per second', 'Metre per second'),
    ('kilometre per hour', 'Kilometre per hour'),
    ('knot', 'knot'),

]


class SpeedConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=SPEED_CHOICES)
    unit_to = forms.ChoiceField(label='Unit to', choices=SPEED_CHOICES)
    unit_value = forms.FloatField(initial=0)
