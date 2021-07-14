from re import X
from checkmath.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from calculations import evaluate
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
        variables = json.loads(request.POST.get("variables"))

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
            answer = evaluate(function, variables)
        except:
            answer = "Nope"

        # vlist = []
        # for v in variables.keys():
        #     vlist.append({
        #         'variable':
        #     })

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