from django.http import HttpResponse, request

# Create your views here.
from django.shortcuts import render


def add_offer(*args, **kwargs):
    print("args: ", *args)
    print("kwargs: ", **kwargs)
    return HttpResponse("aaa")


def offer_list(*args, **kwargs):
    return render(request, "templates/job_list.html", {})
