from django.shortcuts import render
from home.models import Music
# Create your views here.


def home(request):

    #print(Music.objects.get(pk=3))
    #print(Music.objects.all())
    return render(request, 'home.html')