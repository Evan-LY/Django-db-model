from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader
# Create your views here.

def index(request,name):
    template = loader.get_template("index2.html")
    context = {"name":name}
    return HttpResponse(template.render(context,request))

def get_form(request):
    form = request.POST
    print(form)
    return HttpResponse(f"name:{form['name']},gender:{form['gender']},age:{form['age']}")