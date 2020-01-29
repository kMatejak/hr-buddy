from django.http import HttpResponse


# Create your views here.
def register_view(*args, **kwargs):
    return HttpResponse("<h1>Register company site</h1>")
