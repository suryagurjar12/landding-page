from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def index2(request):
    return HttpResponse("<h1 style=color:red>Welcome to home 2 page</h1>")
