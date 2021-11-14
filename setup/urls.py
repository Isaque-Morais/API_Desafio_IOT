from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from cupom.views import CuponsViewSet, ModelosCuponsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cupons', CuponsViewSet, basename='Cupons')
router.register('ModelosNotas', ModelosCuponsViewSet, basename='ModelosNotas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
