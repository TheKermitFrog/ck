from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import songs

def home(request):
    song = songs.objects.all()
    return render(request, 'home.html', {
        'songs' : song,
    })

def previews(request, song_id):
    try:
        song = songs.objects.get(id=song_id)
    except songs.DoesNotExist:
        raise Http404('song not found')
    return render(request, 'previews.html', {
        'songs' : song,
    })

def collection(request):
    song = songs.objects.all()
    return render(request, 'collection.html', {
        'songs' : song,
    })
