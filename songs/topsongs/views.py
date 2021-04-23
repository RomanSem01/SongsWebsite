from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Song, Band, Genre, Playlist, Subscription
from .forms import RegistrationForm, LoginForm, PlaylistCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime


def home(request):
    if request.method == 'POST':
        song = get_object_or_404(
            Song, name=request.POST.get('song_name').strip().split(" (")[0])
        return redirect('song/{}'.format(song.pk))

    songs = Song.objects.all()
    if request.user.is_authenticated:
        subs = request.user.subscription_set.all()
        if len(subs) > 0:
            playlists = subs[0].playlists.all().order_by('-updated')
        else:
            playlists = []
        context = {'songs': songs, 'subs': subs, 'playlists': playlists}
    else:
        context = {'songs': songs}
    return render(request, 'topsongs/home.html', context)


def signup_user(request):
    if request.method == 'GET':
        context = {'form': RegistrationForm()}
        return render(request, 'topsongs/signup_user.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {'form': RegistrationForm(
                ), 'error': 'That username has already been taken'}
                return render(request, 'topsongs/signup_user.html', context)
        else:
            context = {'form': RegistrationForm(
            ), 'error': 'Passwords did not match'}
            return render(request, 'topsongs/signup_user.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {'form': LoginForm()}
        return render(request, 'topsongs/login_user.html', context)
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {
                'form': LoginForm(), 'error': 'Username or password is incorrect'}
            return render(request, 'topsongs/login_user.html', context)

        login(request, user)
        return redirect('home')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def search_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    context = {'song': song}
    return render(request, 'topsongs/search.html', context)


def band_info(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    songs = band.song_set.all()
    context = {'band': band, 'songs': songs}
    return render(request, 'topsongs/band_info.html', context)


@login_required
def create_playlist(request):
    if request.method == 'GET':
        context = {'form': PlaylistCreationForm()}
        return render(request, 'topsongs/create_playlist.html', context)
    else:
        try:
            form = PlaylistCreationForm(request.POST)
            new_playlist = form.save(commit=False)
            new_playlist.user = request.user
            new_playlist.save()
            return redirect('display_playlists')
        except ValueError:
            context = {'form': PlaylistCreationForm(), 'error': 'Bad data'}
            return render(request, 'topsongs/create_playlist.html', context)


@login_required
def remove_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, user=request.user, pk=playlist_id)
    if request.method == 'POST':
        playlist.delete()
        return redirect('display_playlists')


@login_required
def add_to_playlist(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    if request.method == 'GET':
        playlists = get_list_or_404(Playlist, user=request.user)
        print(playlists)
        context = {'playlists': playlists}
        return render(request, 'topsongs/add_to_playlist.html', context)
    else:
        playlist = get_object_or_404(
            Playlist, user=request.user, name=request.POST.get('playlist_name'))
        playlist.updated = datetime.datetime.now()
        playlist.save()
        playlist.songs.add(song)
        return redirect('home')


@login_required
def delete_from_playlist(request, playlist_id, song_id):
    playlist = get_object_or_404(Playlist, user=request.user, pk=playlist_id)
    if request.method == 'POST':
        song = get_object_or_404(Song, pk=song_id)
        playlist.songs.remove(song)
        playlist.save()
        return redirect('playlist_info', playlist_id)


@login_required
def display_playlists(request):
    playlists = Playlist.objects.all().filter(user=request.user)
    context = {'playlists': playlists}
    return render(request, 'topsongs/display_playlists.html', context)


@login_required
def search_playlists(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'topsongs/search_playlists.html')
    else:
        playlists = Playlist.objects.all().filter(
            name__contains=request.POST.get('playlist_name').strip())
        context['playlists'] = playlists
        return render(request, 'topsongs/search_playlists.html', context)


@login_required
def playlist_info(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    songs = playlist.songs.all()
    context = {'playlist': playlist, 'songs': songs}
    return render(request, 'topsongs/playlist_info.html', context)


@login_required
def show_subscriptions(request):
    subs = get_object_or_404(Subscription, user=request.user)
    playlists = subs.playlists.all()
    context = {'playlists': playlists}
    return render(request, 'topsongs/show_subscriptions.html', context)


@login_required
def subscribe(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    if request.method == 'POST':
        if request.user != playlist.user:
            new_sub = Subscription.objects.get_or_create(user=request.user)[0]
            new_sub.save()
            new_sub.playlists.add(playlist)
            new_sub.save()
            return redirect('show_subscriptions')


@login_required
def unsubscribe(request, playlist_id):
    subs = get_object_or_404(Subscription, user=request.user)
    if request.method == 'POST':
        playlist = get_object_or_404(Playlist, pk=playlist_id)
        subs.playlists.remove(playlist)
        subs.save()
        return redirect('show_subscriptions')


@login_required
def show_user(request, user_id):
    author = get_object_or_404(User, pk=user_id)
    playlists = Playlist.objects.all().filter(user=author)
    context = {'author': author, 'playlists': playlists}
    return render(request, 'topsongs/show_user.html', context)
