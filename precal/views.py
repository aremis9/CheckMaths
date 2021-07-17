from django.shortcuts import render

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
                'answer': 'Nope'
            })

    else:
        return render(request, "precal/cstdform.html")