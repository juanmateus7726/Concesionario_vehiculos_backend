import logging
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from .permissions import IsAdminOrReadOnly

logger = logging.getLogger(__name__)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        vehicle = serializer.save()
        logger.info(f"Creado: {vehicle} por {self.request.user.username}")

    def perform_update(self, serializer):
        vehicle = serializer.save()
        logger.info(f"Actualizado: {vehicle} por {self.request.user.username}")

    def perform_destroy(self, instance):
        logger.info(f"Eliminado: {instance} por {self.request.user.username}")
        instance.delete()