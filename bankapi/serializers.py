from django.db.models import fields
from rest_framework import serializers
from . models import Bank, Branche


class BrancheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branche
        # fields = ('ifsc', 'bank_id', 'branch','address', 'city', 'district', 'state')
        fields='__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'name')
