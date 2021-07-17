from django.urls import path
from . import views

app_name = "bscal"
urlpatterns = [
    # /bscal/...
    path("", views.index, name="index"),
    path("limit/", views.limit, name="limit"),
    # path("circle-standard-form/", views.cstdform, name="cstdform"),
    # path("circle-general-form/", views.cgrlform, name="cgrlform"),
    # path("parabola-finding-roots/", views.proots, name="proots")

]