from dataclasses import field
from django.forms import models
from rest_framework import routers, serializers, viewsets

#  Importación de modelos
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('nombre', 'edad')