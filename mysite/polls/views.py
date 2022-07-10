from django.shortcuts import render
from .models import Artist, Song
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import SongForm


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
# Create your views here.
def index(request):

    artist_names = Artist.objects.all()
    context = {'artist_names': artist_names}
    return render(request, 'polls/index.html', context)


def dummy(request, artist_id):
    
        artist_id = request.GET.get('artist_id')
        artist = Artist.objects.get(pk=artist_id)
        return JsonResponse({'artist':artist.name}, status = 200)
        

def create_song(request):
    
    if is_ajax(request):
        print("yes")
        form = SongForm(request.POST)
    else:
        form = SongForm()

    if form.is_valid():
        print("valid")
        form.save()

    context = {
        'form' : form
    }
    return render(request, "polls/song.html", context)