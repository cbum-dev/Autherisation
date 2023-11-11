from rest_framework import serializers
from .models import Cars

class carSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['brand','model','year']