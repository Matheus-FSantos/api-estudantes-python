from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)
print("Opened database successfully")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home Page - API Rest")

@app.route("/students")
def get():
    return "Students not exist"

@app.route("/students/<name>")
def getByName(name):
    if(name == ""):
        return "Student not Exist"
    else:
        return "Student " + name

if(__name__ == "__main__"):
    app.run()