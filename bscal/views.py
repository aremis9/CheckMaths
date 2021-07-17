from django.shortcuts import render
import calculations as calc

# Create your views here.


def index(request):
    return render(request, 'bscal/index.html')


def limit(request):
    pass