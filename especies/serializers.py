from rest_framework import serializers
from especies.models import Especies

class EspeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especies
        fields = '__all__'