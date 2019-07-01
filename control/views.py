from django.http import HttpResponse
from django.template import loader

from control.forms import LengthConverter, VolumeConverter

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


def home(request):

    result = 0

    if request.method == 'POST':

        filled_form = LengthConverter(request.POST)

        if filled_form.is_valid():

            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = unit_value * metre_values[unit] / metre_values[unit_to]
            result = '{} {} are {} {}'.format(unit_value, unit, calculations, unit_to)

    else:

        form = LengthConverter()

    context = {'form': form, 'result': result}

    template = loader.get_template('control/home.html')
    return HttpResponse(template.render(request=request, context=context))


volume_values = {
    'gallon': 0.264172,
    'quart': 1.056688,
    'pint': 2.113376,
    'ounce': 33.814023,
    'litre': 1,
    'cups': 4.226753,
    'tablespoon': 67.628045,
    'tea spoon': 202.884136,
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

    template = loader.get_template('control/volume_converter.html')
    return HttpResponse(template.render(request=request, context=context))
