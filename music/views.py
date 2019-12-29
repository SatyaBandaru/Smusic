from django.shortcuts import render
from music.models import Album, Songs
from django.core.exceptions import ObjectDoesNotExist

def show_albums(request):
    '''get all albums stored in data base and send the data to home.html
       please remove print statements when code commits into production'''
    print('inside')
    Album_data=Album.objects.all()
    return render(request, "music/home.html", {'album_data': Album_data})

def songs_data(request, album_name, songs_id):
    '''get data of the song W.R.T album(key album name) and provide the same
       to songs.html template'''
    if int(songs_id) == 0:
        '''This code runs when user selects the album not song
           once song selects then based on song id song data will be retrive'''
        Album_details=Songs.objects.filter(Album_name=album_name)
        Album_pic=Album.objects.get(Album_name=album_name)
        return render(request, "music/songs.html", {'Album_details': Album_details, "Album_pic":Album_pic, "songs_id" : 0})
    else:
        songs_id=int(songs_id)
        Album_details=Songs.objects.filter(Album_name=album_name)
        Album_pic=Album.objects.get(Album_name=album_name)
        try:
            song_id = Album_details.get(Song_id=songs_id)
        except ObjectDoesNotExist:
            return render(request, "music/songs.html", {'Album_details': Album_details, "Album_pic":Album_pic, "songs_id" : 0})
        return render(request, "music/songs.html", {'Album_details': Album_details, "Album_pic":Album_pic, "songs_id" : song_id})
