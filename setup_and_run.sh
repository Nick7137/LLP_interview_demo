#!/bin/bash

echo "========================================"
echo "Django Fraud Prevention Setup"
echo "========================================"
echo ""

echo "Step 1: Installing dependencies..."
pip install -r requirements.txt || pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error installing from requirements.txt. Trying alternative method..."
    pip install Django djangorestframework django-cors-headers || pip3 install Django djangorestframework django-cors-headers
fi

echo ""
echo "Step 2: Creating database tables..."
python manage.py migrate || python3 manage.py migrate

echo ""
echo "Step 3: Starting development server..."
echo ""
echo "========================================"
echo "Server will start at http://127.0.0.1:8000/"
echo "Press CTRL+C to stop the server"
echo "========================================"
echo ""

python manage.py runserver || python3 manage.py runserver

