from django.shortcuts import render
from home.models import Music
# Create your views here.


def home(request):

    Music.objects.create(song='My Second Trip', singer='去散散步吧')

    print(Music.objects.all())
    return render(request, 'home.html',{
        "data": Music.objects.all()
    })