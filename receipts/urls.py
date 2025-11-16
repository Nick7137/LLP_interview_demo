from django.urls import path
from . import views

urlpatterns = [
    # Mobile app for NFC tapping
    path('mobile/', views.mobile_app, name='mobile_app'),
    
    # Desktop viewer for seeing receipts
    path('desktop/', views.desktop_viewer, name='desktop_viewer'),
    
    # Legacy route - redirects to mobile
    path('', views.mobile_app, name='receipts_list'),
    
    # Receipt detail page
    path('receipt/<str:receipt_number>/', views.receipt_detail, name='receipt_detail'),
    
    # API endpoints
    path('api/nfc-tap/', views.process_nfc_tap, name='process_nfc_tap'),
    path('api/receipts/', views.get_receipts, name='get_receipts'),
]

