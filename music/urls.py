from django.urls import path
from music.api.viewsets import MusicsListAPIView, MusicsDetailAPIView

urlpatterns = [
    path("music-list", MusicsListAPIView.as_view(), name="music_list"),
    path("music-detail/<int:pk>", MusicsDetailAPIView.as_view(), name="music_detail"),
]