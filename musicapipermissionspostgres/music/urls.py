from django.urls import path
from music.api.viewsets import MusicsListAPIView, MusicsDetailAPIView

urlpatterns = [
    path("api/musics-list", MusicsListAPIView.as_view(), name="music_list"),
    path("api/musics-detail/<int:pk>", MusicsDetailAPIView.as_view(), name="music_detail"),
]