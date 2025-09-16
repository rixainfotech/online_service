# RIXA Learning Platform

Django project with frontend landing page, registration (with UPI/UTR), course catalog, and enrollment storage.

## Requirements
- Python 3.11+
- pip

## Setup
```bash
cd sessions
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Apps
- `accounts`: registration, login, profile (UPI/UTR)
- `courses`: course list and enrollment

## URLs
- `/` Home
- `/register/` Register
- `/accounts/login/` Login
- `/courses/` Course list
- `/admin/` Django admin

## Notes
- Default UPI ID is configured in `rixa/settings.py` via `UPI_ID_DEFAULT`.
- Database is `db.sqlite3` (ignored by git).
