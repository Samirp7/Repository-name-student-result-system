# Student Result Management System

A full-stack web application to manage and publish student results, built with **Python Flask** and **MongoDB**.

![Python](https://img.shields.io/badge/Python-3.14-blue) ![Flask](https://img.shields.io/badge/Flask-3.1.3-green) ![MongoDB](https://img.shields.io/badge/MongoDB-latest-brightgreen)

## Features

- Student login — view personal results and GPA
- Admin panel — add students, publish and update results
- Automatic grade and GPA calculation (A+ to F)
- Clean dark-themed UI
- Secure password hashing (SHA-256)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | MongoDB (via PyMongo) |
| Frontend | HTML, CSS, Jinja2 |

## Grade Scale

| Marks | Grade | Grade Point |
|-------|-------|-------------|
| 90-100 | A+ | 4.0 |
| 80-89 | A | 3.7 |
| 70-79 | B+ | 3.3 |
| 60-69 | B | 3.0 |
| 50-59 | C+ | 2.7 |
| 40-49 | C | 2.3 |
| 0-39 | F | 0.0 |

## Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/Samirp7/student-result-system.git
cd student-result-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make sure MongoDB is running locally (port 27017)

# 4. Run the app
python app.py

# 5. Open browser → http://localhost:5000
```

## Default Admin Login

```
Username: admin
Password: admin123
```

## Project Structure

```
student-result-system/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md
├── static/
│   └── css/
│       └── style.css   # Dark theme stylesheet
└── templates/
    ├── base.html
    ├── index.html
    ├── student_login.html
    ├── student_dashboard.html
    ├── admin_login.html
    ├── admin_dashboard.html
    ├── add_student.html
    ├── add_result.html
    └── view_student.html
```

## Author

**Samir Parajuli** — BIT Student, MIT Bagbazar  
GitHub: [@Samirp7](https://github.com/Samirp7)
