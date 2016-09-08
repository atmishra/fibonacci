
from django.template.response import TemplateResponse

from .forms import InputForm

from .getterm import term


def index(request):

    form = InputForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():

            n = form.cleaned_data['n']
            fib_term = term(n)

            context.update({'n': n, 'term': fib_term})

    return TemplateResponse(request, 'pages/home.html', context)

