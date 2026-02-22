## Restaurant Reservation System

A scalable **Django REST API** for managing restaurant reservations.

This project includes:

* Django-powered Admin Dashboard
* JWT Authentication
* Table management (Admin only)
* Double-booking prevention
* Manual reservation status updates

Built with scalability and clean architecture in mind.

---

## Features

* **Admin-only table creation**
* **Reservation system with double-booking protection**
* **Manual reservation status control** (e.g., Pending, Confirmed, Cancelled)
* **JWT-based authentication**
* **Django Admin dashboard for management**

---

## Tech Stack

* Django
* Django REST Framework
* Simple JWT
* SQLite (default, configurable)

---

## Installation

### 1️ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️ Create and activate a virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️ Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist, generate it using:

```bash
pip freeze > requirements.txt
```

But this should be done by the project author before pushing to GitHub.

---

### 4️ Apply migrations

```bash
python manage.py migrate
```

---

### 5️ Create superuser

```bash
python manage.py createsuperuser
```

---

### 6️ Run the server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/admin/
```

---

##  Authentication

JWT authentication is implemented using Django REST Framework Simple JWT.

To obtain a token:

```
POST /api/token/
```

To refresh token:

```
POST /api/token/refresh/
```

Include token in headers:

```
Authorization: Bearer <your_access_token>
```

---

## Future Improvements (Optional Section)

* Automatic reservation status updates
* Email notifications
* Table availability time slots
* Docker support
* Production-ready PostgreSQL configuration
