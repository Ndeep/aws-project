from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h2>You have reached the homepage</h2>")

def type_my_name(request,name):
    return HttpResponse("<h2>Hello,{0}</h2>".format(name))
