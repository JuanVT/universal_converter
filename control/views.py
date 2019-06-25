from django.http import HttpResponse
from django.template import loader

from control.forms import ConverterForm

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

    if request.method == 'GET':

        form = ConverterForm()

    elif request.method == 'POST':

        filled_form = ConverterForm(request.POST)

        if filled_form.is_valid():

            form = filled_form
            unit = form.cleaned_data['unit']
            unit_to = form.cleaned_data['unit_to']
            unit_value = form.cleaned_data['unit_value']

            calculations = form.cleaned_data['unit_value'] * metre_values[unit] / metre_values[unit_to]
            result = '{} {} are {} {}'.format(unit_value, unit, calculations, unit_to)

    context = {'form': form, 'result': result}

    template = loader.get_template('control/home.html')
    return HttpResponse(template.render(request=request, context=context))
