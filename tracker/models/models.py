from django.db import models

from core.models import BaseModel
from tracker.constants import TransactionType


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transaction_category',null=True,blank=True)
    type = models.CharField(max_length=255, choices=TransactionType.choices, default=TransactionType.INCOME)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.type} {self.amount}"
