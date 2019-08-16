from django.http import HttpResponse
from django.template import loader
import requests

from control.forms import LengthConverter, VolumeConverter, TimeConverter, CurrencyConverter, TemperatureConverter, \
    WeightConverter


def home(request):
    context = {}

    template = loader.get_template('control/home.html')
    return HttpResponse(template.render(request=request, context=context))


metre_values = {
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

            calculations = unit_value * metre_values[unit] / metre_values[unit_to]
            result = '{} {}s'.format(calculations, unit_to)

    else:
        form = LengthConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


volume_values = {
    'gallon': 0.264172,
    'quart': 1.056688,
    'pint': 2.113376,
    'ounce': 33.814023,
    'litre': 1,
    'cups': 4.226753,
    'tablespoon': 67.628045,
    'teaspoon': 202.884136,
    'cubic inches': 61.023744,
    'cubic feet': 0.035315,
    'cubic yard': 0.001308,
    'milliliter': 1000,
    'cubic centimeter': 1000,
    'cubic meter': 0.001,
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

            calculations = unit_value * volume_values[unit_to] / volume_values[unit]
            result = '{} {}s'.format(calculations, unit_to)

    else:
        form = VolumeConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


time_values = {
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

            calculations = unit_value * time_values[unit] / time_values[unit_to]
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
                    calculations = 9 / 5 * unit_value + 32

                elif unit_to == 'kelvin':
                    calculations = unit_value + 273.15

                elif unit_to == 'fahrenheit':
                    calculations = (unit_value - 32) * 5 / 9

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

            else:
                result = '{} {}'.format(calculations, unit_to)

    else:
        form = TemperatureConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))


weight_values = {
    'tonne': 10 ** 6,
    'kg': 1000,
    'g': 1,
    'mg': 0.001,
    'micro gram': 10 ** -6,
    'imperial ton': 1016046.91,
    'us ton': 907184.74,
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

            calculations = unit_value * weight_values[unit] / weight_values[unit_to]
            result = '{} {}'.format(calculations, unit_to)

    else:
        form = WeightConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/generic_converter.html')
    return HttpResponse(template.render(request=request, context=context))
