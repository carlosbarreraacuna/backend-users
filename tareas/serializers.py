from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    persona_tipo_documento = serializers.CharField(source='persona.tipo_documento', read_only=True)
    persona_numero_documento = serializers.CharField(source='persona.numero_documento', read_only=True)
    class Meta:
        model = Tarea
        fields = '__all__'