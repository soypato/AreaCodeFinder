from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) # Lo convierte en Flask APP

db = sqlite3.connect("countries.sqlite")
cursor = db.cursor()
db_instruction = cursor.execute("SELECT * from 'codes'")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        area_data_form = request.form.get("area_data_form")
        db_custom_instruction = cursor.execute("SELECT country FROM 'codes' WHERE code = ?", area_data_form)
        return render_template("results.html", area_data_form=area_data_form, db_custom_instruction=db_custom_instruction)
