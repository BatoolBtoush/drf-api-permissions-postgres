from rest_framework import generics
from .serializers import MusicSerializer
from music.models import Music
from .permissions import IsOwnerOrReadOnly


class MusicsListAPIView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsOwnerOrReadOnly, )