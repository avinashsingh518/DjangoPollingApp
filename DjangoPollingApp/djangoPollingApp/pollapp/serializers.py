from .models import *
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields=['emailid', 'firstname', 'lastname','username','mobile','password']
