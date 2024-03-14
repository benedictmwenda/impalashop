from django.shortcuts import render
from .models import Client

# Create your views here.


def index(request):
    data=Client.objects.all()
    context={"data": data}
    return render(request, "index.html", context)
