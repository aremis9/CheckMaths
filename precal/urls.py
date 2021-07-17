from django.urls import path
from . import views

app_name = "precal"
urlpatterns = [
    # /genmath/...
    path("", views.index, name="index"),
    path("graphing/", views.graphing, name="graphing"),
    path("circle-standard-form/", views.cstdform, name="cstdform"),
    path("circle-general-form/", views.cgrlform, name="cgrlform"),
    path("parabola-finding-roots/", views.proots, name="proots")

]