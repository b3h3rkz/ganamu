from rest_framework.serializers import ModelSerializer
from .models import Exchange, Coin
from country.serializers import AdminCountryModelSerializer

class CoinModelSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = ['name', 'website', 'logo', 'symbol']


class AdminCoinModelSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'name', 'symbol', 'website', 'logo', 'active', 'created', 'modified']


class ExchangeModelSerializer(ModelSerializer):
    class Meta:
        country = AdminCountryModelSerializer(read_only=True)
        depth = 1
        model = Exchange
        fields = ['name', 'logo', 'url', 'country', 'coins']


class AdminExchangeModelSerializer(ModelSerializer):
    coins = AdminCoinModelSerializer(many=True, source='name')

    class Meta:
        country = AdminCountryModelSerializer(read_only=True)
        depth = 1
        model = Exchange
        fields = ['id', 'name', 'logo', 'country', 'coins', 'active', 'created', 'modified']


