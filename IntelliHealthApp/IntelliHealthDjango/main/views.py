from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from utils.utils import Client


def api_health(request):
    return HttpResponse("{api_health: \"Success\", version_number: 99}")


def chatgpt(request):
    cur_client = Client()
    text = cur_client.ask_question("How to efficiently learn ai technology?")
    print(text)
    return JsonResponse(text)
