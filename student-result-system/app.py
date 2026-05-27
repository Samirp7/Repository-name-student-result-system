from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = "samir_secret_2024"

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="samir",
        password="1234",
        database="student_results"
    )

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def calc_grade(marks):
    if marks >= 90: return "A+", 4.0
    elif marks >= 80: return "A", 3.7
    elif marks >= 70: return "B+", 3.3
    elif marks >= 60: return "B", 3.0
    elif marks >= 50: return "C+", 2.7
    elif marks >= 40: return "C", 2.3
    else: return "F", 0.0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/student/login", methods=["GET","POST"])
def student_login():
    if request.method == "POST":
        roll = request.form["roll"].strip()
        pw   = hash_pw(request.form["password"])
        db   = get_db(); cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM students WHERE roll=%s AND password=%s", (roll, pw))
        stu = cur.fetchone(); db.close()
        if stu:
            session["student_id"] = stu["id"]
            session["student_name"] = stu["name"]
            session["role"] = "student"
            return redirect(url_for("student_dashboard"))
        flash("Invalid roll number or password.", "error")
    return render_template("student_login.html")

@app.route("/student/dashboard")
def student_dashboard():
    if session.get("role") != "student":
        return redirect(url_for("student_login"))
    db = get_db(); cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM students WHERE id=%s", (session["student_id"],))
    stu = cur.fetchone()
    cur.execute("SELECT * FROM results WHERE student_id=%s", (session["student_id"],))
    results = cur.fetchall(); db.close()
    for r in results:
        r["grade"], r["gp"] = calc_grade(r["marks"])
    gpa = round(sum(r["gp"] for r in results) / len(results), 2) if results else 0
    return render_template("student_dashboard.html", student=stu, results=results, gpa=gpa)

@app.route("/admin/login", methods=["GET","POST"])
def admin_login():
    if request.method == "POST":
        pw  = hash_pw(request.form["password"])
        db  = get_db(); cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (request.form["username"], pw))
        adm = cur.fetchone(); db.close()
        if adm:
            session["admin"] = True
            session["role"]  = "admin"
            return redirect(url_for("admin_dashboard"))
        flash("Invalid credentials.", "error")
    return render_template("admin_login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    db = get_db(); cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.execute("SELECT COUNT(*) as total FROM students")
    total = cur.fetchone()["total"]; db.close()
    return render_template("admin_dashboard.html", students=students, total=total)

@app.route("/admin/add-student", methods=["GET","POST"])
def add_student():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    if request.method == "POST":
        db = get_db(); cur = db.cursor()
        try:
            cur.execute("INSERT INTO students (name,roll,batch,password) VALUES (%s,%s,%s,%s)",
                (request.form["name"].strip(), request.form["roll"].strip(),
                 request.form["batch"].strip(), hash_pw(request.form["password"])))
            db.commit(); flash("Student added!", "success")
            return redirect(url_for("admin_dashboard"))
        except: flash("Roll number already exists!", "error")
        finally: db.close()
    return render_template("add_student.html")

@app.route("/admin/add-result", methods=["GET","POST"])
def add_result():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    db = get_db(); cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    if request.method == "POST":
        sid   = request.form["student_id"]
        subj  = request.form["subject"].strip()
        marks = int(request.form["marks"])
        cur.execute("SELECT * FROM results WHERE student_id=%s AND subject=%s", (sid, subj))
        existing = cur.fetchone()
        if existing:
            cur.execute("UPDATE results SET marks=%s WHERE student_id=%s AND subject=%s", (marks, sid, subj))
        else:
            cur.execute("INSERT INTO results (student_id,subject,marks) VALUES (%s,%s,%s)", (sid, subj, marks))
        db.commit(); db.close()
        flash("Result saved!", "success")
        return redirect(url_for("admin_dashboard"))
    db.close()
    return render_template("add_result.html", students=students)

@app.route("/admin/student/<int:sid>")
def view_student(sid):
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    db = get_db(); cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM students WHERE id=%s", (sid,))
    stu = cur.fetchone()
    cur.execute("SELECT * FROM results WHERE student_id=%s", (sid,))
    results = cur.fetchall(); db.close()
    for r in results:
        r["grade"], r["gp"] = calc_grade(r["marks"])
    gpa = round(sum(r["gp"] for r in results) / len(results), 2) if results else 0
    return render_template("view_student.html", student=stu, results=results, gpa=gpa)

@app.route("/admin/delete/<int:sid>")
def delete_student(sid):
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    db = get_db(); cur = db.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (sid,))
    db.commit(); db.close()
    flash("Student deleted.", "success")
    return redirect(url_for("admin_dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)