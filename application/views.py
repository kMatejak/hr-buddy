from django.http import HttpResponse


# Create your views here.
def application(*args, **kwargs):
    return HttpResponse("<h1>application</h1>")
