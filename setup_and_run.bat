@echo off
echo ========================================
echo Django Fraud Prevention Setup
echo ========================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error installing dependencies. Trying alternative method...
    pip install Django djangorestframework django-cors-headers
)

echo.
echo Step 2: Creating database tables...
python manage.py migrate

echo.
echo Step 3: Starting development server...
echo.
echo ========================================
echo Server will start at http://127.0.0.1:8000/
echo Press CTRL+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause

