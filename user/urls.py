from django.urls import path
from . import views

urlpatterns = [
    # path("",views.index,name="index"),
    path("index/<str:name>",views.index,name="index"),
    path("form",views.get_form,name="form")
]