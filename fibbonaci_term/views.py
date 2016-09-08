
from django.template.response import TemplateResponse

from .forms import InputForm
# from mymodules import getterm


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():

            n = form.cleaned_data['n']
            fib_term = term(n)

            context = {
                'n': n,
                'term': fib_term,
                'form': form,

            }

    elif request.method == 'GET':

        form = InputForm()

        context = {


            'form': form,

        }
    return TemplateResponse(request, 'pages/home.html', context)


def term(n):

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
