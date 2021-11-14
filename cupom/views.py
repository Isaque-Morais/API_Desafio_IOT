from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.serializers import Serializer
from cupom.models import Cupom, ModeloNota
from cupom.serializer import CupomSerializer, ModelosNotasSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CuponsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cupons Fiscais para doação"""
    queryset = Cupom.objects.all()
    serializer_class = CupomSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ModelosCuponsViewSet(viewsets.ModelViewSet):
    """Exibindo os modelos de Cupons Doado"""
    queryset = ModeloNota.objects.all()
    serializer_class = ModelosNotasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    