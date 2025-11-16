from django.db import models
from django.utils import timezone
import uuid


class ReceiptItem(models.Model):
    """Individual item in a receipt"""
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='receipt_items')
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['id']


class Transaction(models.Model):
    """Transaction/Receipt model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    receipt_number = models.CharField(max_length=50, unique=True, db_index=True)
    merchant_name = models.CharField(max_length=200, default='Demo Merchant')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['-timestamp']),
            models.Index(fields=['receipt_number']),
        ]
    
    def __str__(self):
        return f"{self.merchant_name} - {self.receipt_number} - ${self.total_amount}"

