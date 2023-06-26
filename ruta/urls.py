from django.urls import path, include
from ruta import views
#from .views import RutaView, RutaDetailView, MovilidadView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ruta', views.RutaViewSet)
router.register(r'movilidad', views.MovilidadViewSet)

urlpatterns = [
    path('', include(router.urls))
]
