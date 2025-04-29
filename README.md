# Health Information System (Flask + MySQL)

This is a lightweight Health Information System built with **Flask**, **MySQL**, and **HTML/CSS** to help healthcare providers register clients, manage health programs, enroll clients into programs, and view client profiles.

---

##  Demo & Slides

- **Video Demo**: [Watch Prototype Demo](https://your-video-link.com)
- **Project Slides**: [View Slide Presentation](https://your-slide-link.com)

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

