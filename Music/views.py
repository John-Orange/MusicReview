from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from. models import MusicType, Author, Song
from. forms import MTForm, AuthorForm, SongForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'Music/index.html')

def songs(request):
    songs_list=Song.objects.all()
    return render(request, 'Music/songs.html', {'songs_list': songs_list})

def songDetail(request, id):
    song=get_object_or_404(Song, pk=id)
    return render(request, 'Music/songDetail.html',{'song': song})

@login_required
def newMusicType(request):
    form=MTForm

    if request.method=='POST':
        form=MTForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MTForm()
    else:
        form=MTForm()
    return render(request, 'Music/newMusicType.html', {'form':form})

@login_required
def newAuthor(request):
    form=AuthorForm

    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=AuthorForm()
    else:
        form=AuthorForm()
    return render(request, 'Music/newAuthor.html', {'form':form})

@login_required
def newSong(request):
    form=SongForm

    if request.method=='POST':
        form=SongForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=SongForm()
    else:
        form=SongForm()
    return render(request, 'Music/newSong.html', {'form':form})

def loginmessage(request):
    return render(request, 'Music/loginmessage.html')

def logoutmessage(request):
    return render(request, 'Music/logoutmessage.html')