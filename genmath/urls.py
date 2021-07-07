from django.urls import path
from . import views

urlpatterns = [
    # /genmath/...
    path("", views.index, name="index")
]