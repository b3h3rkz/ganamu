# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from .models import Coin, Exchange


class CoinAdmin(admin.ModelAdmin):
    class Meta:
        model = Coin
        fields = ['id', 'name', 'website', 'symbol', 'logo', 'active']
        list_display = ['id', 'name', 'website', 'symbol', 'logo', 'active']


class ExchangeAdmin(admin.ModelAdmin):
    class Meta:
        model = Exchange
        fields = ['id', 'name', 'url', 'country', 'active', 'created', 'modified']
        list_display = ['id', 'name', 'url',  'active', 'created', 'modified']
        # list_display = [f.name for f in Exchange._meta.get_fields()]


admin.site.register(Coin, CoinAdmin)
admin.site.register(Exchange, ExchangeAdmin)
