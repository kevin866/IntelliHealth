from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def api_health(request):
    return HttpResponse("{api_health: \"Success\", version_number: 99}")


def chatgpt(request):
    return HttpResponse("another test")
