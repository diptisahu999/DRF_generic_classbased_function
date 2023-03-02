from rest_framework import serializers
from . models import Student


class Serializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
        # fields=['name','email']

        