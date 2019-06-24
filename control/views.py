from django.http import HttpResponse
from django.template import loader

from control.forms import ConverterForm


def home(request):
    form = ConverterForm()
    context = {'form': form}

    template = loader.get_template('control/home.html')
    return HttpResponse(template.render(request=request, context=context))
