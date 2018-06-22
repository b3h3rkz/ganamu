from rest_framework.serializers import (ModelSerializer,)
from .models import Country


class CountryModelSerializer(ModelSerializer):
    """
    Country model Serializer for public view
    """
    class Meta:
        model = Country
        fields = ['id', 'name', 'iso_code', 'currency', 'flag']


class AdminCountryModelSerializer(ModelSerializer):
    """
     Country model Serializer for Admin Access
    """

    class Meta:
        model = Country
        fields = ['id', 'name', 'iso_code', 'currency', 'flag', 'active']

