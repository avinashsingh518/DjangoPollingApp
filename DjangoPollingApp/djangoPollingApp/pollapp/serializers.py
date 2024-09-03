
from .models import *
from rest_framework import serializers



"""<----------API View Decorator , Model Serializer-----APIVIew Serializer-------start---->"""
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        exclude=['password']



"""<----------API View Decorator , Model Serializer-----APIVIew Serializer-----end------>"""