from django.urls import path
from . import views

app_name = "genmath"
urlpatterns = [
    # /genmath/...
    path("", views.index, name="index"),
    path("function-evaluation/", views.fevaluation, name="fevaluation")
]