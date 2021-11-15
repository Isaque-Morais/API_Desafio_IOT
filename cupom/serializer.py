from django.db.models import fields
from rest_framework import serializers
from cupom.models import Cupom, ModeloNota

class CupomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupom
        fields = ('id', 'numero_cupom', 'cnpj', 'cpf_doador', 'valor_compra', 'data', 'entidade_doacao')
        
class ModelosNotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloNota
        fields = '__all__'