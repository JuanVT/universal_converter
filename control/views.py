from django.http import HttpResponse
from django.template import loader
import requests

from control.forms import (
    LengthConverter,
    VolumeConverter,
    TimeConverter,
    CurrencyConverter,
    TemperatureConverter,
    WeightConverter,
    SpeedConverter)


def home(request):
    context = {}

    template = loader.get_template('control/home.html')
    return HttpResponse(template.render(request=request, context=context))


METRE_VALUES = {
    'kilometre': 1000.0,
    'metre': 1.0,
    'centimetre': 0.01,
    'millimetre': 0.001,
    'micrometre': 10 ** -6.0,
    'nanometre': 10 ** -9.0,
    'mile': 1609.34,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254,
}


def length_converter(request):
    result = 0

    if request.method == 'POST':
        filled_form = LengthConverter(request.POST)

        if filled_form.is_valid():
            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = unit_value * METRE_VALUES[unit] / METRE_VALUES[unit_to]
            result = '{} {}s'.format(calculations, unit_to)

    else:
        form = LengthConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


VOLUME_VALUES = {
    'gallon': 0.264172,
    'quart': 1.056688,
    'pint': 2.113376,
    'ounce': 33.814023,
    'litre': 1,
    'cup': 4.226753,
    'tablespoon': 67.628045,
    'teaspoon': 202.884136,
    'cubic_inch': 61.023744,
    'cubic_feet': 0.035315,
    'cubic_yard': 0.001308,
    'milliliter': 1000,
    'cubic_centimetre': 1000,
    'cubic_metre': 0.001,
}


def volume_converter(request):
    result = 0

    if request.method == 'POST':
        filled_form = VolumeConverter(request.POST)

        if filled_form.is_valid():
            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = unit_value * VOLUME_VALUES[unit_to] / VOLUME_VALUES[unit]
            result = '{} {}s'.format(calculations, unit_to)

    else:
        form = VolumeConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


TIME_VALUES = {
    'nanosecond': 10 ** -9,
    'microsecond': 1 ** -6,
    'millisecond': 0.001,
    'second': 1,
    'minute': 60,
    'hour': 3600,
    'day': 86400,
    'week': 604800,
    'month': 2628000,
    'year': 31556952,
    'decade': 315569520,
    'century': 3155695200,
}


def time_converter(request):
    result = 0

    if request.method == 'POST':
        filled_form = TimeConverter(request.POST)

        if filled_form.is_valid():
            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = unit_value * TIME_VALUES[unit] / TIME_VALUES[unit_to]
            result = '{} {}s'.format(calculations, unit_to)

    else:
        form = TimeConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


def currency_converter(request):
    result = 0

    if request.method == 'POST':
        filled_form = CurrencyConverter(request.POST)

        if filled_form.is_valid():
            form = filled_form
            unit = form.cleaned_data['unit'].upper()
            unit_to = form.cleaned_data['unit_to'].upper()
            unit_value = form.cleaned_data['unit_value']

            url = 'https://api.exchangeratesapi.io/latest?base=' + unit
            currency_values = requests.get(url).json()

            try:
                currency_value = currency_values['rates'][unit_to]

            except KeyError:
                currency_value = 1

            finally:
                calculations = unit_value * currency_value
                result = '{} {}'.format(calculations, unit_to)
    else:
        form = CurrencyConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


def temperature_converter(request):
    result = 0

    if request.method == 'POST':
        filled_form = TemperatureConverter(request.POST)

        if filled_form.is_valid():
            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = unit_value

            if unit == 'celsius':
                if unit_to == 'fahrenheit':
                    calculations = (1.8 * unit_value) + 32

                elif unit_to == 'kelvin':
                    calculations = unit_value + 273.15

            elif unit == 'fahrenheit':
                if unit_to == 'celsius':
                    calculations = (unit_value - 32) * 5 / 9

                elif unit_to == 'kelvin':
                    calculations = (unit_value + 459.67) * 5 / 9

            elif unit == 'kelvin':
                if unit_to == 'celsius':
                    calculations = unit_value - 273.15

                elif unit_to == 'fahrenheit':
                    calculations = (unit_value * 9 / 5) - 459.67

            result = '{} {}'.format(calculations, unit_to)

    else:
        form = TemperatureConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


WEIGHT_VALUES = {
    'tonne': 10 ** 6,
    'kg': 1000,
    'g': 1,
    'mg': 0.001,
    'micro_gram': 10 ** -6,
    'imperial_ton': 1016046.91,
    'us_ton': 907184.74,
    'stone': 6350.29,
    'pound': 453.592,
    'ounce': 28.349500000294
}


def weight_converter(request):
    result = 0

    if request.method == 'POST':
        filled_form = WeightConverter(request.POST)

        if filled_form.is_valid():
            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = unit_value * WEIGHT_VALUES[unit] / WEIGHT_VALUES[unit_to]
            result = '{} {}'.format(calculations, unit_to)

    else:
        form = WeightConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


SPEED_VALUES = {
    'mile_per_hour': 1,
    'foot_per_second': 1.46667,
    'metre_per_second': 0.44704,
    'kilometre_per_hour': 1.60934,
    'knot': 0.868976,
}


def speed_converter(request):
    result = 0

    if request.method == 'POST':
        filled_form = SpeedConverter(request.POST)

        if filled_form.is_valid():
            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = unit_value * SPEED_VALUES[unit_to] / SPEED_VALUES[unit]
            result = '{} {}'.format(calculations, unit_to)

    else:
        form = SpeedConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))
