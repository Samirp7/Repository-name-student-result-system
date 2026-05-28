# Student Result Management System

A full-stack web application to manage and publish student results, built with **Python Flask** and **MySQL**.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.3-green)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)

---

## 🚀 Features

* Student login — view personal results and GPA
* Admin panel — add students, publish and update results
* Automatic grade and GPA calculation (A+ to F)
* Clean dark-themed UI
* Secure password hashing (SHA-256)

---

## 🛠️ Tech Stack

| Layer    | Technology        |
| -------- | ----------------- |
| Backend  | Python, Flask     |
| Database | MySQL             |
| Frontend | HTML, CSS, Jinja2 |

---

## 📊 Grade Scale

| Marks  | Grade | Grade Point |
| ------ | ----- | ----------- |
| 90-100 | A+    | 4.0         |
| 80-89  | A     | 3.7         |
| 70-79  | B+    | 3.3         |
| 60-69  | B     | 3.0         |
| 50-59  | C+    | 2.7         |
| 40-49  | C     | 2.3         |
| 0-39   | F     | 0.0         |

---

## ⚙️ Setup & Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Samirp7/Repository-name-student-result-system.git
```

### 2️⃣ Open Project Folder

```bash
cd Repository-name-student-result-system/student-result-system
```

### 3️⃣ Install Requirements

```bash
pip install flask mysql-connector-python
```

---

## 🗄️ MySQL Database Setup

Open MySQL Workbench and run:

```sql
CREATE DATABASE student_results;

USE student_results;

CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll VARCHAR(20) UNIQUE NOT NULL,
    batch VARCHAR(20) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    marks INT NOT NULL,
    FOREIGN KEY (student_id)
    REFERENCES students(id)
    ON DELETE CASCADE
);

INSERT INTO admins(username, password)
VALUES ('admin', SHA2('admin123',256));
```

---

## 🔐 Configure Database Connection

Inside `app.py`:

```python
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="samir",
        password="1234",
        database="student_results"
    )
```

Change username/password according to your MySQL setup.

---

## ▶️ Run the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 🔑 Default Admin Login

```text
Username: admin
Password: admin123
```

---

## 📁 Project Structure

```text
student-result-system/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   └── css/
│       └── style.css
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

---

## 📸 Screenshots

Add screenshots here later:

* Home Page
* Admin Dashboard
* Student Dashboard
* Result Page

---

## 🎯 Future Improvements

* PDF result export
* Student photo upload
* Search & filter
* Attendance system
* Charts and analytics
* Dark/light theme switch

---

## 👨‍💻 Author

**Samir Parajuli** — BIT Student, MIT Bagbazar

GitHub: https://github.com/Samirp7

---

## 📄 License

This project is for educational and portfolio purposes.
