from django.urls import path
from . import views

app_name = "precal"
urlpatterns = [
    # /genmath/...
    path("", views.index, name="index"),
    path("circle-standard-form/", views.cstdform, name="cstdform"),
    path("circle-general-form/", views.cgrlform, name="cgrlform"),
    # path("parabola/", views.parabola, name="parabola")

]