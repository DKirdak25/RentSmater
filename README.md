RentSmarter
RentSmarter is a Django-based rental management platform designed to streamline property listing, tenant registration, and secure account verification.
🚧 Status: Pre-Launch (Development Phase)
Overview
RentSmarter provides:
User registration with email verification
Secure authentication system
SMTP-based email delivery
Scalable project structure
Production-ready configuration (Render deployment planned)
This project is currently under active development.
Tech Stack
Python 3.x
Django
PostgreSQL (planned for production)
SMTP Email (SendGrid compatible)
Render (planned deployment)
Project Structure
Copy code

project_root/
│
├── accounts/              # Authentication & user logic
├── core/                  # Shared services (email service, utilities)
├── templates/             # HTML templates
├── static/                # Static source files (CSS, JS)
├── manage.py
└── requirements.txt
Features (Current)
User signup
Email verification system
Token-based activation links
Configurable email backend
Production-ready settings structure
Environment Variables
Create a .env file in the root directory:
Copy code

SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password
Never commit this file.
Installation
1. Clone Repository
Bash
Copy code
git clone https://github.com/yourusername/RentSmarter.git
cd RentSmarter
2. Create Virtual Environment
Bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux / Mac
3. Install Dependencies
Bash
Copy code
pip install -r requirements.txt
4. Run Migrations
Bash
Copy code
python manage.py migrate
5. Run Development Server
Bash
Copy code
python manage.py runserver
Static Files
Static files are managed using:
Copy code

STATIC_ROOT = BASE_DIR / "staticfiles"
In production:
Bash
Copy code
python manage.py collectstatic --noinput
staticfiles/ is excluded from version control.
Deployment Plan
Deployment target: Render
Build command:
Bash
Copy code
python manage.py collectstatic --noinput
Environment variables will be configured inside Render dashboard.
Security Notes
DEBUG will be set to False in production
ALLOWED_HOSTS will be configured at deployment
Secret keys are stored in environment variables
Password authentication for GitHub is disabled (token/SSH required)
Upcoming Features
Property listing system
Tenant dashboard
Role-based permissions
Payment integration
API layer
License
This project is currently private and under development.
