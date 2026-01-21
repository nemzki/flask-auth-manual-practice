# Flask Authentication Practice

## Project Description
This is a practice project to implement user authentication using **Flask**.  
It demonstrates the basic workflow of user registration, login, and dashboard access with form validation, CSRF protection, and route management.

### Key Features
- User registration with input validation
- Secure login with password hashing
- Flash messages for errors and success
- CSRF protection via Flask-WTF

---

## Directory Structure

```text
flask-auth-manual-practice/
│
├─ forms/
│ ├─ __init__.py
│ ├─ login_form.py # Login form with validation
│ └─ register_form.py # Registration form with validation
│
├─ models/
│ ├─ __init__.py
│ ├─ database.py # SQLite database handling
│ └─ user.py # User model and database operations
│
├─ routes/
│ ├─ __init__.py
│ ├─ dashboard.py # Dashboard route
│ ├─ login_routes.py # Login routes and logic
│ └─ register_routes.py # Registration routes and logic
│
├─ static/
│ ├─ auth.css # Authentication form styles
│ └─ style.css # Global styles
│
├─ templates/
│ ├─ auth_base.html # Base template for auth pages
│ ├─ base.html # Main base template
│ ├─ dashboard.html
│ ├─ login.html
│ └─ register.html
│
├─ app.py # Main Flask application
├─ auth.db # SQLite database
├─ requirements.txt
└─ README.md
```

---

## Technologies Used
- Python 3.x
- Flask
- Flask-WTF
- Werkzeug
- SQLite3
- HTML / CSS (templates and styling)

---

## Setup Instructions
### 1. Clone the repository
```bash
git clone <repository_url>
cd flask-auth-manual-practice
```


### 2. Create and activate a virtual environment

- Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

- macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Access the app

Open your browser and go to:

http://localhost:5000

### Usage

- Register a new account via the registration page.

- Login with your credentials.

- Access the dashboard after successful login.

- Flash messages display form errors or success messages.

## File Notes

### Forms

- register_form.py → Fields: first name, last name, username, email, password, confirm password

- login_form.py → Fields: username/email and password

### Models

- user.py → User model and helper functions

- database.py → SQLite database setup and queries

### Routes

- register_routes.py → Handles registration

- login_routes.py → Handles login

- dashboard.py → Protected dashboard route

### Templates

- auth_base.html → Base layout for auth pages

- register.html, login.html, dashboard.html → Page-specific templates

### Static

- auth.css → Styles for authentication forms

- style.css → Global styles, including universal box-sizing

### Known Issues / Limitations

- No password reset functionality

- No email verification

- Dashboard content is minimal for practice purposes