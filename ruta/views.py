
from rest_framework import viewsets
from .models import TblMovilidadRuta
from .serializer import TblMovilidadRutaSerializer

class MovilidadRutaViewSet(viewsets.ModelViewSet):
    queryset = TblMovilidadRuta.objects.all()
    serializer_class = TblMovilidadRutaSerializer
