import json
import os
from django.conf import settings
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from casefactory.settings import STATIC_ROOT

# Create your views here.


def get_brands(request):
    brands = os.listdir(os.path.join(STATIC_ROOT, "mockup_image"))
    return JsonResponse(brands,safe=False)


def get_models(request, brand):
    models_raw = os.listdir(os.path.join(STATIC_ROOT,"mockup_image", brand))
    models = []
    for model in models_raw:
        if model != "Default_Mobile_Mockup.png":
            models.append(model.replace("___Sublime.png", "" ))
    return JsonResponse(models, safe=False)


# /static/mockup_image/honor/{model}___Sublime.png