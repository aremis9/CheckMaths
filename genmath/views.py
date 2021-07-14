from checkmath.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse
from calculations import evaluate
import os
import json


ROOT = os.path.abspath(os.curdir)

# Create your views here.
def index(request):
    return render(request, 'genmath/index.html')

def fevaluation(request):
    if request.method == "POST":
        function = request.POST.get("function")
        variables = json.loads(request.POST.get("variables"))

        if not function or not variables:
            return render(request, 'genmath/fevaluation.html', {
                'answer': 'Nope'
            })

        try:
            answer = evaluate(function, variables)
        except:
            answer = "Nope"


        return render(request, 'genmath/fevaluation.html', {
            'answer': answer
        })


    else:
        return render(request, 'genmath/fevaluation.html')