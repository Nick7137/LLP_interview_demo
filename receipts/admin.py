from django.contrib import admin
from .models import Transaction, ReceiptItem


class ReceiptItemInline(admin.TabularInline):
    model = ReceiptItem
    extra = 1


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'merchant_name', 'total_amount', 'timestamp']
    list_filter = ['timestamp', 'merchant_name']
    search_fields = ['receipt_number', 'merchant_name']
    readonly_fields = ['id', 'timestamp']
    inlines = [ReceiptItemInline]


@admin.register(ReceiptItem)
class ReceiptItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit_price', 'line_total']
    search_fields = ['name']

