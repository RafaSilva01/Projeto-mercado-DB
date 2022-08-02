from rest_framework import serializers
from usuarios import models

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__' 