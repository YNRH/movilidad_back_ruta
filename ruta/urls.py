from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ruta', views.MovilidadRutaViewSet, basename='ruta')

urlpatterns = router.urls
