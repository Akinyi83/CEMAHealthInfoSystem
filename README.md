# Health Information System (Flask + MySQL)

This is a lightweight Health Information System built with **Flask**, **MySQL**, and **HTML/CSS** to help healthcare providers register clients, manage health programs, enroll clients into programs, and view client profiles.

---

##  Demo & Slides

- **Video Demo**: [Watch Prototype Demo](https://drive.google.com/file/d/14cDvOwrAwktVKSsz21h6z-AB2Oo2DkZp/view?usp=sharing)
- **Project Slides**: [View Slide Presentation](https://docs.google.com/presentation/d/1nDzr1NNKOfb8RU5uQ9Qwz6DnlCbBurlzQW4wPcOKVwQ/edit?usp=sharing)

---

## ⚙️ Features

-  Register new clients (patients)
-  Create and list health programs
-  Enroll clients into health programs
-  View client profile with enrollment history
-  Search client by email
-  RESTful API and browser-based forms
-  Clean project structure with separation of concerns

---

## 🗂 Project Structure

```bash
.
├── static/                   # CSS and JS files
├── templates/                # HTML templates
│   ├── dashboard.html
│   ├── clients.html
│   ├── programs.html
│   └── ...
├── app.py                    # Main Flask app
├── routes.py                 # All HTTP route logic
├── models.py                 # Database functions (CRUD)
├── db_config.py              # MySQL DB connection settings
├── requirements.txt          # Python package dependencies
└── README.md                 # Project documentation

##1. Clone the Repository

git clone https://github.com/your-username/CEMAHealthInfoSystem.git
cd health-info-system

##2.Install Dependencies
pip install -r requirements.txt

##3. Set Up MySQL Database
CREATE DATABASE cema_health_system;
## Update .env with your own database credentials.

##4. RUN THE APP

python app.py

# API Endpoints
Endpoint	Method	Description
/api/client	GET	Get all clients
/api/clients	POST	Add a new client
/api/clients/search?name=	GET	Search client by name
/api/clients/<client_id>	GET	View client details + enrollments
/api/programs	GET	Get all health programs
/api/programs	POST	Add new health program(s)
/api/enrollments	GET	Get all enrollments
/api/enrollments	POST	Enroll client into a program

#How to Test
You can test the API endpoints using tools like:

 Postman: for POST/GET API calls.

 Browser: visit rendered HTML templates.

 Curl: for quick command-line API tests.

# Technologies Used
Python 3.x

Flask

MySQL

HTML/CSS (Jinja2 templates)

Postman (for testing)