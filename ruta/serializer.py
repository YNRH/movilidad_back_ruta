from rest_framework import serializers
from .models import TblMovilidadRuta, TblMovilidad

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovilidadRuta
        fields = '__all__'

class MovilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovilidad
        fields = '__all__'



    '''
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['movilidad_id'] = "movilidad" + instance.movilidad_id
        return representation
    '''

