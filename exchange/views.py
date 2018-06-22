from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Exchange, Coin
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import (
    ExchangeModelSerializer,
    AdminExchangeModelSerializer,
    CoinModelSerializer,
    AdminCoinModelSerializer)


class ExchangeModelViewSet(ReadOnlyModelViewSet):
    model = Exchange
    serializer_class = ExchangeModelSerializer
    queryset = Exchange.objects.all()


class AdminExchangeModelViewSet(ModelViewSet):
    model = Exchange
    serializer_class = AdminExchangeModelSerializer
    queryset = Exchange.objects.all()
    permission_classes = [IsAdminUser]


class CoinModelViewSet(ReadOnlyModelViewSet):
    model = Coin
    serializer_class = CoinModelSerializer
    queryset = Coin.objects.all()


class AdminCoinModelViewSet(ModelViewSet):
    model = Coin
    serializer_class = AdminCoinModelSerializer
    queryset = Coin.objects.all()
    permission_classes = [IsAdminUser]
