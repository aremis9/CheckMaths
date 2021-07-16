from django.urls import path
from . import views

app_name = "precal"
urlpatterns = [
    # /genmath/...
    path("", views.index, name="index"),
    # path("circle/", views.circle, name="circle"),
    # path("parabola/", views.parabola, name="parabola")

]