import json
import os
from django.conf import settings
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from casefactory.settings import STATIC_ROOT

# Create your views here.


def get_brands(request):
    brands = os.listdir(os.path.join(STATIC_ROOT, "mockup", "static"))
    return JsonResponse(brands,safe=False)

def model_list(request):
    json_data = open(os.path.join(settings.STATIC_ROOT, 'source.json'))
    json_data = json.load(json_data)
    model_list = []
    for i in json_data["data"]["product_attribute_values"]:
        model_list.append({"id": i["id"],"model":i["product"]["mockups"][0]["front_mockup"]})
    return JsonResponse(model_list, safe=False)


def get_model_by_id(request, id):
    json_data = open(os.path.join(settings.STATIC_ROOT, 'source.json'))
    json_data = json.load(json_data)
    for i in json_data["data"]["product_attribute_values"]:
        if id == i["id"]:
            return JsonResponse(i, safe=False)



def get_model_list(request, id):
    url = "https://qikink.com/erp2/index.php/sizes/get_size_models"

    payload={
    'category_id': str(id),
    'gender_id': ' 5_5'
    }
    files=[

    ]
    headers = {
        'Cookie': 'ci_session=d5536f102e911d40933b085b0dad434a4da967ae'
    }

    serverResponse = requests.request("POST", url, headers=headers, data=payload, files=files)
    return JsonResponse(serverResponse.json()["list"], safe=False)


def get_model_from_qikink(request, id):
    url = "https://qikink.com/erp2/index.php/mockup/get_mockup_mobile_new"
    payload={'gender': '5_5',
    'category': '105',
    'size': str(id)
    }
    files=[

    ]
    headers = {
    # 'Cookie': 'ci_session=d5536f102e911d40933b085b0dad434a4da967ae'
    }

    server_response = requests.request("POST", url, headers=headers, data=payload, files=files)
    product = json.loads(server_response.json()["products"])[0][0]
    mockup = {
        "title": product["title"],
        "mockup": product["thumbnail"]
    }
    return JsonResponse(mockup, safe=False)
