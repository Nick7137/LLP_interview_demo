# Django Fraud Prevention MVP

A Django-based implementation of the corporate credit card fraud prevention system with NFC card tapping functionality.

## Features

- **NFC Card Tapping**: Employees tap their corporate credit card on an Android phone
- **Automatic Receipt Generation**: Receipts are automatically created and stored in the database
- **Itemized Receipt Display**: Detailed breakdown of all purchased items
- **Database Storage**: All transactions stored in SQLite (can be changed to PostgreSQL/MySQL)
- **REST API**: API endpoints for NFC tap processing and receipt retrieval
- **Admin Interface**: Django admin for managing transactions and receipts

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project directory:**
   ```bash
   cd LLP_interview_demo-main/LLP_interview_demo-main
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations to create database tables:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Main page: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## Project Structure

```
fraud_prevention/
├── fraud_prevention/          # Main project directory
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
├── receipts/                  # Receipts app
│   ├── models.py             # Transaction and ReceiptItem models
│   ├── views.py              # Views and API endpoints
│   ├── urls.py               # App URL configuration
│   ├── admin.py              # Admin interface configuration
│   └── templates/            # HTML templates
│       └── receipts/
│           ├── list.html     # Receipts list page
│           └── detail.html   # Receipt detail page
├── manage.py                  # Django management script
└── requirements.txt          # Python dependencies
```

## Database Models

### Transaction
- `id`: UUID primary key
- `receipt_number`: Unique receipt identifier
- `merchant_name`: Name of the merchant
- `amount`: Transaction amount (before tax)
- `tax_amount`: Tax amount
- `total_amount`: Total amount (amount + tax)
- `currency`: Currency code (default: USD)
- `timestamp`: Transaction timestamp

### ReceiptItem
- `name`: Item name
- `quantity`: Quantity purchased
- `unit_price`: Price per unit
- `line_total`: Total for this line item

## API Endpoints

### POST `/api/nfc-tap/`
Process NFC card tap and create a receipt.

**Request Body:**
```json
{
    "amount": 12.75,
    "merchantName": "Demo Coffee"
}
```

**Response:**
```json
{
    "success": true,
    "receipt_number": "123456789",
    "transaction_id": "uuid-here",
    "amount": 13.77,
    "message": "Receipt created successfully"
}
```

### GET `/api/receipts/`
Get list of all receipts.

**Response:**
```json
{
    "success": true,
    "receipts": [
        {
            "id": "uuid",
            "receipt_number": "123456789",
            "merchant_name": "Demo Merchant",
            "total_amount": 13.77,
            "timestamp": "2024-01-01T12:00:00Z"
        }
    ]
}
```

## Usage

1. **Open the application** in Chrome on an Android device (over HTTPS for NFC to work)
2. **Tap the screen once** to enable NFC scanning
3. **Hold an NFC card/tag** near the phone
4. The receipt will be automatically created and appear in the list
5. **Click on any receipt** to view the detailed itemized breakdown

## Admin Interface

Access the Django admin at `/admin/` to:
- View all transactions
- View receipt items
- Search and filter transactions
- Manage data directly

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

## Production Deployment

For production deployment:

1. **Change SECRET_KEY** in `settings.py`
2. **Set DEBUG = False**
3. **Configure ALLOWED_HOSTS**
4. **Use a production database** (PostgreSQL recommended)
5. **Set up static file serving**
6. **Use HTTPS** (required for Web NFC API)
7. **Configure CORS** properly for your domain

## Database Options

The default database is SQLite. To use PostgreSQL or MySQL:

1. Install the database adapter:
   ```bash
   # For PostgreSQL:
   pip install psycopg2-binary
   
   # For MySQL:
   pip install mysqlclient
   ```

2. Update `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',  # or mysql
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

## Notes

- Web NFC API requires Chrome on Android with HTTPS
- The NFC scanning happens client-side in the browser
- Receipt data is sent to the Django backend via API
- All transactions are stored in the database
- Itemized receipts are automatically generated based on transaction amount

