from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def index1(request):
    return HttpResponse("<h1 style=color:yellow>Welcome to home 1 page</h1>")
