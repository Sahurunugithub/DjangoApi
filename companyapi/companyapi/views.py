from django.http import HttpResponse, JsonResponse
import json

def home_page(request):
    print("home page requested")
    return HttpResponse("This is Home page made by preeti")

def company_page(request):
    print("company requested")
    friends=[
        "preeti",
        "ankita",
        "anjali"
    ]
    return JsonResponse(friends,safe=False)