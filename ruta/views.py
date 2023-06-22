
from rest_framework import generics
from .models import TblMovilidadRuta
from .serializer import RutaSerializer

class RutaView(generics.ListCreateAPIView):
    queryset = TblMovilidadRuta.objects.all()
    serializer_class = RutaSerializer

class RutaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TblMovilidadRuta.objects.all()
    serializer_class = RutaSerializer


'''
from rest_framework import viewsets
from .models import TblMovilidadRuta
from .serializer import TblMovilidadRutaSerializer

class MovilidadRutaViewSet(viewsets.ModelViewSet):
    queryset = TblMovilidadRuta.objects.all()
    serializer_class = TblMovilidadRutaSerializer
'''