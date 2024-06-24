from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("<h1 style=color:blue>Welcome to home page</h1>")

# def index(request):
#     return JsonResponse("<h1 style=color:blue>Welcome to home page</h1>")
