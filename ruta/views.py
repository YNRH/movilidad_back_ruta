
from .models import TblMovilidadRuta, TblMovilidad
from .serializer import RutaSerializer, MovilidadSerializer

from rest_framework import viewsets

class RutaViewSet(viewsets.ModelViewSet):
    queryset = TblMovilidadRuta.objects.all()
    serializer_class = RutaSerializer

class MovilidadViewSet(viewsets.ModelViewSet):
    queryset = TblMovilidad.objects.all()
    serializer_class = MovilidadSerializer

