from rest_framework import viewsets
from usuarios.api import serializers
from usuarios import models


class UsuarioViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.UsuariosSerializers
    queryset = models.Usuario.objects.all()