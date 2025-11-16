# Quick Start Guide - Running the Django Website

## Step 1: Navigate to the Project Directory

Open your terminal/command prompt and navigate to the project folder:

```bash
cd LLP_interview_demo-main/LLP_interview_demo-main
```

## Step 2: Create a Virtual Environment (Recommended)

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If you get an error, try:
```bash
pip install Django djangorestframework django-cors-headers
```

## Step 4: Set Up the Database

Run migrations to create the database tables:

```bash
python manage.py migrate
```

## Step 5: (Optional) Create Admin User

To access the admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

## Step 6: Run the Development Server

```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Step 7: Access the Website

Open your web browser and go to:

- **Main Receipts Page**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## For NFC Testing (Android)

1. Make sure your Django server is accessible over HTTPS (required for Web NFC)
2. For local testing, you can use a tool like `ngrok` to create an HTTPS tunnel:
   ```bash
   ngrok http 8000
   ```
3. Use the HTTPS URL provided by ngrok on your Android device
4. Open Chrome browser on Android
5. Tap the screen once to enable NFC
6. Hold an NFC card/tag near the phone

## Troubleshooting

### Port Already in Use
If port 8000 is busy, use a different port:
```bash
python manage.py runserver 8080
```

### Module Not Found Errors
Make sure you're in the correct directory and have activated your virtual environment.

### Database Errors
If you get database errors, try:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Permission Errors (Linux/Mac)
You might need to use `python3` instead of `python`:
```bash
python3 manage.py runserver
```

## Stopping the Server

Press `CTRL+C` (or `CTRL+Break` on Windows) in the terminal to stop the server.

