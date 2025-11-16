from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import random
from decimal import Decimal

from .models import Transaction, ReceiptItem


def receipts_list(request):
    """Main page showing list of receipts (legacy - redirects to mobile)"""
    return render(request, 'receipts/mobile.html')


def mobile_app(request):
    """Mobile NFC tapping interface"""
    return render(request, 'receipts/mobile.html')


def desktop_viewer(request):
    """Desktop/laptop receipt viewer interface"""
    return render(request, 'receipts/desktop.html')


def receipt_detail(request, receipt_number):
    """Display detailed itemized receipt"""
    transaction = get_object_or_404(Transaction, receipt_number=receipt_number)
    items = transaction.receipt_items.all()
    context = {
        'transaction': transaction,
        'items': items,
    }
    return render(request, 'receipts/detail.html', context)


@api_view(['POST'])
@csrf_exempt
def process_nfc_tap(request):
    """
    API endpoint to process NFC card tap and create a receipt
    Expected JSON payload:
    {
        "amount": 12.75,
        "merchantName": "Demo Coffee" (optional)
    }
    """
    try:
        data = json.loads(request.body)
        amount = Decimal(str(data.get('amount', 12.75)))
        merchant_name = data.get('merchantName', 'Demo Merchant')
        
        # Generate receipt number
        receipt_number = str(random.randint(100000000, 999999999))
        
        # Ensure receipt number is unique
        while Transaction.objects.filter(receipt_number=receipt_number).exists():
            receipt_number = str(random.randint(100000000, 999999999))
        
        # Calculate tax (8%)
        tax_amount = amount * Decimal('0.08')
        total_amount = amount + tax_amount
        
        # Create transaction
        transaction = Transaction.objects.create(
            receipt_number=receipt_number,
            merchant_name=merchant_name,
            amount=amount,
            tax_amount=tax_amount,
            total_amount=total_amount,
            currency='USD',
            timestamp=timezone.now()
        )
        
        # Generate itemized items based on amount
        items = generate_itemized_items(amount)
        
        # Create receipt items and associate with transaction
        for item_data in items:
            ReceiptItem.objects.create(
                transaction=transaction,
                name=item_data['name'],
                quantity=item_data['quantity'],
                unit_price=Decimal(str(item_data['unit_price'])),
                line_total=Decimal(str(item_data['line_total']))
            )
        
        return Response({
            'success': True,
            'receipt_number': receipt_number,
            'transaction_id': str(transaction.id),
            'amount': float(total_amount),
            'message': 'Receipt created successfully'
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_receipts(request):
    """API endpoint to get list of receipts"""
    transactions = Transaction.objects.all().order_by('-timestamp')[:100]  # Get 100 most recent
    receipts_data = []
    
    for tx in transactions:
        receipts_data.append({
            'id': str(tx.id),
            'receipt_number': tx.receipt_number,
            'merchant_name': tx.merchant_name,
            'amount': float(tx.amount),
            'tax_amount': float(tx.tax_amount),
            'total_amount': float(tx.total_amount),
            'currency': tx.currency,
            'timestamp': tx.timestamp.isoformat(),
        })
    
    return Response({
        'success': True,
        'receipts': receipts_data
    })


def generate_itemized_items(amount):
    """Generate realistic itemized items based on transaction amount"""
    items = []
    amount_decimal = Decimal(str(amount))
    amount_float = float(amount)
    
    if amount_float >= 50:
        # Large purchase - multiple items
        item_types = [
            {'name': 'Office Supplies - Paper', 'base_price': 12.99},
            {'name': 'Office Supplies - Pens', 'base_price': 8.50},
            {'name': 'Office Supplies - Folders', 'base_price': 15.00},
            {'name': 'Business Meal', 'base_price': 25.00},
            {'name': 'Client Entertainment', 'base_price': 30.00},
            {'name': 'Travel Expense - Parking', 'base_price': 10.00},
            {'name': 'Travel Expense - Fuel', 'base_price': 35.00}
        ]
        
        remaining = amount_float * 0.92  # Leave room for tax
        num_items = min(4, max(2, int(amount_float / 20)))
        
        for i in range(num_items):
            if remaining <= 5:
                break
            item_type = random.choice(item_types)
            qty = random.choice([1, 1, 1, 2, 3])  # Mostly 1, sometimes more
            price = min(item_type['base_price'] * qty, remaining * 0.6)
            price = round(price, 2)
            
            items.append({
                'name': item_type['name'],
                'quantity': qty,
                'unit_price': Decimal(str(round(item_type['base_price'], 2))),
                'line_total': Decimal(str(round(price, 2)))
            })
            remaining -= price
        
        if remaining > 2:
            items.append({
                'name': 'Miscellaneous Expense',
                'quantity': 1,
                'unit_price': Decimal(str(round(remaining, 2))),
                'line_total': Decimal(str(round(remaining, 2)))
            })
            
    elif amount_float >= 20:
        # Medium purchase
        items.append({
            'name': 'Business Meal',
            'quantity': 1,
            'unit_price': Decimal(str(round(amount_float * 0.7, 2))),
            'line_total': Decimal(str(round(amount_float * 0.7, 2)))
        })
        items.append({
            'name': 'Beverages',
            'quantity': 1,
            'unit_price': Decimal(str(round(amount_float * 0.3, 2))),
            'line_total': Decimal(str(round(amount_float * 0.3, 2)))
        })
    elif amount_float >= 10:
        # Small-medium purchase
        qty = random.choice([1, 2])
        items.append({
            'name': 'Coffee & Pastries',
            'quantity': qty,
            'unit_price': Decimal(str(round(amount_float * 0.9 / qty, 2))),
            'line_total': Decimal(str(round(amount_float * 0.9, 2)))
        })
    else:
        # Small purchase
        items.append({
            'name': 'Coffee & Snacks',
            'quantity': 1,
            'unit_price': Decimal(str(round(amount_float, 2))),
            'line_total': Decimal(str(round(amount_float, 2)))
        })
    
    return items

