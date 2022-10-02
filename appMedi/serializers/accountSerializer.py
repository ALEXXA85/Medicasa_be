from dataclasses import field
from appMedi.models.account import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        #field = ['balance','lastChangeDate','isActive']
        exclude =('user'),
        #fields = ('')