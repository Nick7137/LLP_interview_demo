# Run All Commands - Quick Reference

## Windows (Command Prompt or PowerShell)

### Option 1: Run the batch file
```bash
setup_and_run.bat
```

### Option 2: Run commands manually
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Option 3: One-liner (PowerShell)
```powershell
pip install -r requirements.txt; python manage.py migrate; python manage.py runserver
```

## macOS/Linux (Terminal)

### Option 1: Run the shell script
```bash
chmod +x setup_and_run.sh
./setup_and_run.sh
```

### Option 2: Run commands manually
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Option 3: One-liner
```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py runserver
```

## If Python 3 is required (use python3 instead of python)

### Windows:
```bash
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

### macOS/Linux:
```bash
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## Complete Setup (First Time Only)

If this is your first time running the project, you might also want to create an admin user:

```bash
python manage.py createsuperuser
```

Then run the server:
```bash
python manage.py runserver
```

## Access the Website

Once the server is running:
- **Main Page**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Stop the Server

Press `CTRL+C` in the terminal to stop the server.

