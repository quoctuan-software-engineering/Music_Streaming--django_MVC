from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),

    path('profile/', views.user_profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),

    path('album/', views.user_albums, name='albums'),
    path('album/<int:album_id>/detail/', views.album_detail, name='album_detail'),
    path('album/create/', views.create_album, name='create_album'),
    path('album/<int:album_id>/delete/', views.delete_album, name='delete_album'),
    path('album/<int:album_id>/remove-song/<int:song_id>/', views.remove_song_album, name='remove_song_album'),

    path('song/favorites/', views.user_favorites, name='favorites'),
    path('song/<int:song_id>/detail/', views.song_detail, name='song_detail'),
    path('song/search/', views.search, name='search'),
    path('song/<int:song_id>/song-favorites/', views.song_favorite, name='song_favorites'),
    path('song/<int:song_id>/song-albums/', views.song_album, name='song_albums'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
