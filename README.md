# 🏥 HealthCare API

A Django REST Framework-based backend for managing **Patients, Doctors, and their Mappings**, with JWT authentication support.

---

## 🚀 Features

- 🔐 **JWT Authentication** (Login, Token Refresh)  
- 👨‍⚕️ **Doctor Management** (CRUD APIs)  
- 🧑‍🤝‍🧑 **Patient Management** (CRUD APIs)  
- 🔗 **Doctor–Patient Mapping**  
- 📑 **RESTful API Endpoints** with `DRF`  
- 🛠 **PostgreSQL/MySQL/SQLite Support** (configurable)  

---

## 🏗 Tech Stack

- [Python 3.10+](https://www.python.org/)  
- [Django 5.x](https://www.djangoproject.com/)  
- [Django REST Framework](https://www.django-rest-framework.org/)  
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)  
- [PostgreSQL](https://www.postgresql.org/)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/HealthCare.git
cd HealthCare
2. Create & activate virtual environment
bash
Copy code
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Create superuser
bash
Copy code
python manage.py createsuperuser
6. Start server
bash
Copy code
python manage.py runserver
🔑 Authentication (JWT)
Obtain token
http
Copy code
POST /api/auth/
{
  "username": "your_username",
  "password": "your_password"
}
Response:

json
Copy code
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
Refresh token
http
Copy code
POST /api/auth/refresh/
{
  "refresh": "<refresh_token>"
}
📌 API Endpoints
Patients
GET /api/patients/ → List all patients
POST /api/patients/ → Create a new patient
GET /api/patients/{id}/ → Get patient by ID
PUT /api/patients/{id}/ → Update patient (all fields)
DELETE /api/patients/{id}/ → Delete patient

Doctors
GET /api/doctors/ → List all doctors
POST /api/doctors/ → Create doctor
GET /api/doctors/{id}/ → Get doctor by ID
PUT /api/doctors/{id}/ → Update doctor
DELETE /api/doctors/{id}/ → Delete doctor

Mappings
GET /api/mappings/ → List doctor–patient mappings
POST /api/mappings/ → Create mapping

🛠 Example Patient Create (Postman)
Request:

http
Copy code
POST /api/patients/
Authorization: Bearer <access_token>
Content-Type: application/json
Body:

json
Copy code
{
  "name": "Azam",
  "age": 20,
  "address": "Lucknow",
  "contact": 9243567822,
  "gender": "male",
  "condition": "fever"
}
