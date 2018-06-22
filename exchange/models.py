from django.db import models
import uuid
from country.models import Country


class Coin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
    symbol = models.CharField(max_length=5, unique=True)
    website = models.URLField(max_length=100, unique=True, blank=True, null=True)
    logo = models.URLField(max_length=100, unique=True, blank=True, null=True)
    # exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, related_name="exchange")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Exchange(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
    url = models.URLField(max_length=100, unique=True, blank=True, null=True)
    logo = models.URLField(max_length=100, unique=True, blank=True, null=True)
    country = models.ManyToManyField(Country, related_name="countries")
    coins = models.ManyToManyField(Coin, related_name="coins", null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    """
    Each exchange will have a many price instances generated each time a data is fetched from the exchange
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, related_name="exchange")
    btc_price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, null=True)
    ltc_price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, null=True)
    eth_price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, null=True)
    bch_price = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id







