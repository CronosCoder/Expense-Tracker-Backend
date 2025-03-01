from rest_framework import serializers

from tracker.models import Transaction
from tracker.serializers.category_serializers import CategorySerializer


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id","type","category","amount"]

class TransactionDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ["id","type","category","amount", "is_active"]