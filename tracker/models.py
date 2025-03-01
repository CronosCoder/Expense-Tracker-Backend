from django.db import models
from tracker.constants import TransactionType



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transaction_category',null=True,blank=True)
    type = models.CharField(max_length=255, choices=TransactionType.choices, default=TransactionType.INCOME)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
