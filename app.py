from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) # Lo convierte en Flask APP

db = sqlite3.connect("countries.sqlite",check_same_thread=False)
cursor = db.cursor()
db_instruction = cursor.execute("SELECT * from 'codes'")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        area_data_form = request.form.get("area_data_form")
        if not area_data_form or area_data_form.isnumeric() == False:
            message = "Please enter a valid area code."
            return render_template("error.html", message=message)
        try:
            db_custom_instruction = cursor.execute("SELECT country FROM 'codes' WHERE code = ?", (area_data_form,)).fetchall()
            db_row_country = db_custom_instruction[0][0]
            return render_template("results.html", area_data_form=area_data_form, db_row_country=db_row_country)
        except IndexError as e:
            message = "The code you entered does not correspond to any country."
            return render_template("error.html",message=message)

