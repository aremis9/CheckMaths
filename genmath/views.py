from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    text = "Line 1 <br/> Line 2 <br/> Line 3"
    return render(request, 'genmath/index.html', {
        'text': text
    })

def fevaluation(request):
    return render(request, 'genmath/fevaluation.html')