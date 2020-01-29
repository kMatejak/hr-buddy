from django.http import HttpResponse


# Create your views here.
def add_offer(*args, **kwargs):
    return HttpResponse("<h1>add offer site</h1>")
