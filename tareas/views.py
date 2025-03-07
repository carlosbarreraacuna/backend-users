from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.decorators import action
from .models import Tarea
from .serializers import TareaSerializer
from datetime import datetime

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fecha_limite', 'persona__tipo_documento', 'persona__numero_documento']
    
    @action(detail=False, methods=['get'])
    def por_rango_fechas(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        
        if fecha_inicio and fecha_fin:
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
                fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
                
                tareas = Tarea.objects.filter(fecha_limite__range=[fecha_inicio, fecha_fin])
                serializer = self.get_serializer(tareas, many=True)
                return Response(serializer.data)
            except ValueError:
                return Response({"error": "Formato de fecha incorrecto. Usar YYYY-MM-DD"}, status=400)
        return Response({"error": "Se requieren los parámetros fecha_inicio y fecha_fin"}, status=400)
    
    @action(detail=False, methods=['get'])
    def por_persona(self, request):
        tipo_documento = request.query_params.get('tipo_documento')
        numero_documento = request.query_params.get('numero_documento')
        
        if tipo_documento and numero_documento:
            tareas = Tarea.objects.filter(
                persona__tipo_documento=tipo_documento,
                persona__numero_documento=numero_documento
            )
            serializer = self.get_serializer(tareas, many=True)
            return Response(serializer.data)
        return Response({"error": "Se requieren los parámetros tipo_documento y numero_documento"}, status=400)