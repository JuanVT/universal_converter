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
    ("gallon", "Gallon"),
    ("quart", "Quart"),
    ("ounce", "Ounce"),
    ("litre", "Litre"),
    ("cup", "Cup"),
    ("tablespoon", "Tablespoon"),
    ("teaspoon", "Teaspoon"),
    ("pint", "Pint"),
    ("cubic_inch", "Cubic inch"),
    ("cubic_feet", "Cubic Feet"),
    ("cubic_yard", "Cubic yard"),
    ("milliliter", "Milliliter"),
    ("cubic_centimetre", "Cubic centimetre"),
    ("cubic_metre", "Cubic metre")
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
    ('g', 'Grams'),
    ('mg', 'Milligram'),
    ('micro_gram', 'Micro gram'),
    ('imperial_ton', 'Imperial ton'),
    ('us_ton', 'US ton'),
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
    ('mile_per_hour', 'Mile per hour'),
    ('foot_per_second', 'Foot per second'),
    ('metre_per_second', 'Metre per second'),
    ('kilometre_per_hour', 'Kilometre per hour'),
    ('knot', 'Knot'),
]


class SpeedConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=SPEED_CHOICES)
    unit_to = forms.ChoiceField(label='Unit to', choices=SPEED_CHOICES)
    unit_value = forms.FloatField(initial=0)
