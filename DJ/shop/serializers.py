from rest_framework import serializers

from shop.models import *


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
