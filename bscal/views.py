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


def differential(request):
    pass