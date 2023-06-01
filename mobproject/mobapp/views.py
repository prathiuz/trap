from django.shortcuts import render
from django.shortcuts import render
from .models import place, profile


# Create your views here.

def demo(request):
    obj = place.objects.all()
    obc = profile.objects.all()
    return render(request, "index.html", {'result': obj,'aj': obc})
