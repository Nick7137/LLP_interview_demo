# Corporate Credit Card Fraud Prevention MVP

A proof-of-concept system for fraud prevention using NFC-enabled corporate credit cards. This MVP allows employers to verify that employee purchases align with company policy by providing itemized receipts for each transaction.

## Overview

This system enables:
1. **NFC Card Tapping**: Employees tap their corporate credit card on an Android phone
2. **Receipt Number Entry**: After the tap, employees enter a receipt/transaction number
3. **Itemized Receipt Display**: The system routes to a bank website that displays a detailed, itemized receipt showing all purchased items
4. **Fraud Prevention**: Employers can review itemized purchases to verify compliance with company spending policies

## How It Works

### Flow

1. **NFC Tap** (`toast_simulator.html`)
   - Employee taps their NFC-enabled corporate card on an Android phone
   - The system detects the card and processes the transaction
   - Transaction data is stored locally with a unique receipt number

2. **Receipt Number Entry**
   - After successful tap, the system prompts for a receipt number
   - A receipt number is auto-generated and pre-filled (can be edited)
   - User can enter any receipt/transaction number

3. **Bank Receipt View** (`bank.html`)
   - System routes to the bank website with the receipt number
   - Bank website displays a detailed, itemized receipt including:
     - Transaction ID
     - Merchant name
     - Date and time
     - Itemized list of all purchased items (quantity, name, price)
     - Subtotal, tax, and total amounts
     - Fraud prevention compliance note

## Files

- **`toast_simulator.html`**: Main NFC card reader interface
  - Handles NFC card detection using Web NFC API
  - Manages transaction flow and receipt number entry
  - Stores transaction data in browser localStorage

- **`bank.html`**: Bank receipt display page
  - Accepts receipt/transaction number via URL parameter
  - Retrieves transaction data and displays itemized receipt
  - Shows detailed breakdown for fraud prevention review

- **`tx.json`**: Sample transaction data (fallback)

## Requirements

- **Android device** with NFC capability
- **Chrome browser** (Web NFC API support)
- **HTTPS connection** (required for Web NFC API)

## Usage

1. Open `toast_simulator.html` in Chrome on an Android device over HTTPS
2. Tap the screen once to enable NFC scanning
3. Hold an NFC card/tag near the phone to simulate a card tap
4. After approval, enter the receipt number (auto-filled, can be edited)
5. Click "View Receipt" to navigate to the bank website
6. Review the itemized receipt for fraud prevention compliance

## Technical Details

### Transaction Storage
- Transactions are stored in browser `localStorage` (MVP implementation)
- Each transaction includes:
  - Unique transaction ID
  - Receipt number (user-friendly identifier)
  - Transaction amount
  - Merchant information
  - Itemized list of purchased items
  - Tax and total amounts
  - Timestamp

### Receipt Lookup
- The system supports lookup by:
  - Receipt number (primary)
  - Transaction ID
  - Direct transaction key

### Itemized Receipt Generation
- The system automatically generates realistic itemized receipts based on transaction amount
- Categories include:
  - Office Supplies
  - Business Meals
  - Travel Expenses
  - Client Entertainment
  - And more

## Future Enhancements

For a production system, consider:
- Server-side transaction storage and retrieval
- Integration with actual bank/payment processor APIs
- Real-time receipt data from merchants
- Policy compliance checking automation
- Reporting and analytics dashboard
- Multi-user authentication and authorization
- Mobile app instead of web app

## Notes

- This is an MVP/demo system
- Transaction data is stored locally in the browser
- NFC functionality requires Chrome on Android with HTTPS
- In production, this would integrate with actual payment processors and bank systems
