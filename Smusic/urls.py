"""Smusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from music import views
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('albums/', views.show_albums),
    #url(r'albums/(?P<album_name>[A-Z,a-z,_]+)/$', views.songs_data),
    url(r'albums/(?P<album_name>[A-Z,a-z,_]+)/(?P<songs_id>[0-9]+)/$', views.songs_data),
    #url(r'^(?P<pk>[0-9]+)/$', views.play, name='play_songs')
]

# Path for media files from where templates gets the source files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
