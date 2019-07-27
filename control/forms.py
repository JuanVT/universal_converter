from django import forms

length_choices = [
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
    unit = forms.ChoiceField(label='Unit', choices=length_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=length_choices)
    unit_value = forms.FloatField(initial=0)


volume_choices = [
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
    unit = forms.ChoiceField(label='Unit', choices=volume_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=volume_choices)
    unit_value = forms.FloatField(initial=0)


time_choices = [
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
    unit = forms.ChoiceField(label='Unit', choices=time_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=time_choices)
    unit_value = forms.FloatField(initial=0)


currency_choices = [
    ('eur', 'EUR'),
    ('cad', 'CAD'),
    ('hkd', 'HKD'),
    ('isk', 'ISK'),
    ('php', 'PHP'),
    ('dkk', 'DKK'),
    ('huf', 'HUF'),
    ('czk', 'CZK'),
    ('aud', 'AUD'),
    ('ron', 'RON'),
    ('sek', 'SEK'),
    ('idr', 'IDR'),
    ('inr', 'INR'),
    ('brl', 'BRL'),
    ('rub', 'RUB'),
    ('hrk', 'HRK'),
    ('jpy', 'JPY'),
    ('thb', 'THB'),
    ('chf', 'CHF'),
    ('sgd', 'SGD'),
    ('pln', 'PLN'),
    ('bgn', 'BGN'),
    ('try', 'TRY'),
    ('cny', 'CNY'),
    ('nok', 'NOK'),
    ('nzd', 'NZD'),
    ('zar', 'ZAR'),
    ('usd', 'USD'),
    ('mxn', 'MXN'),
    ('ils', 'ILS'),
    ('gbp', 'GBP'),
    ('krw', 'KRW'),
    ('myr', 'MYR')
]


class CurrencyConverter(forms.Form):
    unit = forms.ChoiceField(label='Unit', choices=currency_choices)
    unit_to = forms.ChoiceField(label='Unit to', choices=currency_choices)
    unit_value = forms.FloatField(initial=0)
