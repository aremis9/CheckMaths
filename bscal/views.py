from django.shortcuts import render
import calculations as calc

# Create your views here.


def index(request):
    return render(request, 'bscal/index.html')


def limits(request):
    if request.method == "POST":

        function = request.POST.get("function")
        c = request.POST.get("c")

        if not function or not c: 
            return render(request, "bscal/limits.html", {
                'function': '',
                'c': '',
                'answer': 'Nope'
            })

        try:
            answer = calc.getlimit(function, c)
        except:
            answer = 'Nope'
        

        return render(request, "bscal/limits.html", {
                'function': function,
                'c': c,
                'answer': answer
            })

    else:
        return render(request, 'bscal/limits.html')


def differentiation(request):
    if request.method == "POST":

        function = request.POST.get("function")
        nth = request.POST.get("nth")

        if not function:
            return render(request, "bscal/differentiation.html", {
                'function': '',
                'nth': '1',
                'answer': 'Nope'
            })

        try:
            nth = int(nth)
        except:
            return render(request, "bscal/differentiation.html", {
                'function': function,
                'nth': '1',
                'answer': 'Nope'
            })

        try:
            answer = calc.differentiate(function, nth)
        except:
            answer = 'Nope'


        return render(request, "bscal/differentiation.html", {
            'function': function,
            'nth': str(nth),
            'answer': answer
        })


    else:
        return render(request, 'bscal/differentiation.html', {
            'function': '-4x^2 - 5x - 2',
            'nth': '1',
        })

