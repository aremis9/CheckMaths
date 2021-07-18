from re import X
from checkmath.settings import BASE_DIR
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
import calculations as calc
import os
import json


ROOT = os.path.abspath(os.curdir)

# Create your views here.
def index(request):
    return render(request, 'genmath/index.html')


def fevaluation(request):
    x = 4
    if request.method == "POST":
        function = request.POST.get("function")
        try:
            variables = json.loads(request.POST.get("variables"))
        except:
            return render(request, 'genmath/fevaluation.html', {
                'function': 'x^2 + 6x + 9',
                'x': x,
                'answer': 'Nope'
            })

        if 'x' not in variables:
            x = 0
        else:
            x = variables['x']

        if not function or not variables:
            return render(request, 'genmath/fevaluation.html', {
                'function': 'x^2 + 6x + 9',
                'x': x,
                'answer': 'Nope'
            })
        

        try:
            answer = calc.evaluate(function, variables)
        except:
            answer = "Nope"


        return render(request, 'genmath/fevaluation.html', {
            'function': function,
            'x': x,
            'variables': variables,
            'answer': answer
        })


    else:
        return render(request, 'genmath/fevaluation.html', {
            'x': x,
            'function': 'x^2 + 6x + 9'
        })


def foperations(request):
    selectedop = '1'
    if request.method == "POST":
        operations = {
            '1': '+',
            '2': '-',
            '3': '*',
            '4': '/'
        }

        try:
            function1 = request.POST.get("function1")
            function2 = request.POST.get("function2")
            x = request.POST.get("variable-x")
            operation = request.POST.get("operation")
            selectedop = 'option' + operation
        except:
            return render(request, 'genmath/foperations.html', {
                'function1': 'x^2 + 6x + 8',
                'function2': 'x + 2',
                'x': 'x',
                f'{selectedop}': 'selected',
                'answer': 'Nope'
            })

        if not function1 or not function2:
            return render(request, 'genmath/foperations.html', {
                'function1': '',
                'function2': '',
                'x': '',
                f'{selectedop}': 'selected',
                'answer': 'Nope'
            })

        if not x:
            x = 'x'

        if operation not in operations.keys():
            return render(request, 'genmath/foperations.html', {
                'function1': function1,
                'function2': function2,
                'x': x,
                f'{selectedop}': 'selected',
                'answer': 'Invalid operation! Maybe try not to inspect the element?'
            })

        for key, value in operations.items():
            if operation == key:
                operation = value

        try:
            answer = calc.operate(function1, function2, x, operation)
        except:
            answer = "Nope"


        return render(request, 'genmath/foperations.html', {
                'function1': function1,
                'function2': function2,
                'x': x,
                f'{selectedop}': 'selected',
                'answer': answer
            })

    else:
        return render(request, 'genmath/foperations.html', {
            'function1': 'x^2 + 6x + 8',
            'function2': 'x + 2',
            f'{selectedop}': 'selected',
            'x': 'x',
        })


def fcomposite(request):
    
    if request.method == "POST":

        try:
            function1 = request.POST.get("function1")
            function2 = request.POST.get("function2")
            x = request.POST.get("variable-x")
        except:
            return render(request, 'genmath/fcomposite.html', {
                'function1': '3x + 2',
                'function2': '2x^2 + 5',
                'x': '2',
                'answer': 'Nope'
            })

        if not function1 or not function2:
            return render(request, 'genmath/fcomposite.html', {
                'function1': '',
                'function2': '',
                'x': '',
                'answer': 'Nope'
            })

        if not x:
            x = 'x'

        try:
            answer = calc.composite(function1, function2, x)
        except:
            answer = "Nope"


        return render(request, 'genmath/fcomposite.html', {
                'function1': function1,
                'function2': function2,
                'x': x,
                'answer': answer
            })
    else:
        return render(request, 'genmath/fcomposite.html', {
                'function1': '3x + 2',
                'function2': '2x^2 + 5',
                'x': '2',
            })