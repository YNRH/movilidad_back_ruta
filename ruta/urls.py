from django.urls import path
from .views import RutaView, RutaDetailView

urlpatterns = [
    path('ruta/', RutaView.as_view(), name='ruta-list'),
    path('ruta/<int:pk>/', RutaDetailView.as_view(), name='ruta-detail'),
]
