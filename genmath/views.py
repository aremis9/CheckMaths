from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'genmath/index.html')

def fevaluation(request):
    if request.method == "POST":
        function = request.POST.get("function")
        variables = json.loads(request.POST.get("variables"))

        if not function or not variables:
            pass



    return render(request, 'genmath/fevaluation.html')