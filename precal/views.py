from django.shortcuts import render
import calculations as calc

# Create your views here.


def index(request):
    return render(request, 'precal/index.html')


def cstdform(request):
    if request.method == "POST":
        xcoord = request.POST.get("xcoord")
        ycoord = request.POST.get("ycoord")
        radius = request.POST.get("radius")

        if not xcoord or not ycoord or not radius:
            return render(request, "precal/cstdform.html", {
                'xcoord': '5',
                'ycoord': '-2',
                'radius': '3',
                'answer': 'Nope'
            })

        try:
            answer = calc.cstdform(xcoord, ycoord, radius)
        except:
            answer = 'Nope'

        
        return render(request, "precal/cstdform.html", {
            'xcoord': xcoord,
            'ycoord': ycoord,
            'radius': radius,
            'answer': answer
        })

    else:
        return render(request, "precal/cstdform.html", {
            'xcoord': '5',
            'ycoord': '-2',
            'radius': '3',
        })


def cgrlform(request):
    if request.method == "POST":
        xcoord = request.POST.get("xcoord")
        ycoord = request.POST.get("ycoord")
        radius = request.POST.get("radius")

        if not xcoord or not ycoord or not radius:
            return render(request, "precal/cgrlform.html", {
                'xcoord': '5',
                'ycoord': '-2',
                'radius': '3',
                'answer': 'Nope'
            })

        try:
            answer = calc.cgrlform(xcoord, ycoord, radius)
        except:
            answer = 'Nope'

        return render(request, "precal/cgrlform.html", {
            'xcoord': xcoord,
            'ycoord': ycoord,
            'radius': radius,
            'answer': answer
        })

    else:
        return render(request, "precal/cgrlform.html", {
            'xcoord': '5',
            'ycoord': '-2',
            'radius': '3',
        })


def graphing(request):
    if request.method == "POST":
        function = request.POST.get("function")

        if not function:
            return render(request, "precal/graphing.html", {
                'function': '',
                'answer': 'Nope'
            })

        try:
            answer = calc.evaluate(function, {})
        except:
            answer = 'Nope'
            return render(request, "precal/graphing.html", {
                'function': function,
                'answer': 'Nope'
            })

        return render(request, "precal/graphing.html", {
            'function': function
        })

    else:
        return render(request, "precal/graphing.html", {
            'function': '(x + 2)^2 + (y - 1)^2 = 25'
        })


def proots(request):
    if request.method == "POST":
        function = request.POST.get("function")

        if not function:
            return render(request, "precal/proots.html", {
                'function': '',
                'answer': 'Nope'
            })

        try:
            answer = calc.findx(function)
        except:
            answer = 'Nope'

        return render(request, "precal/proots.html", {
                'function': function,
                'answer': answer
            })

    else:
        return render(request, 'precal/proots.html', {
            'function': '2x^2 - 8x + 6',
        })