from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__) # Lo convierte en Flask APP

db = sqlite3.connect("db/paises.sqlite")
cur = db.cursor()

# https://inloop.github.io/sqlite-viewer/#

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        area_data_form = request.form.get("area_data_form")
        res = cur.execute("SELECT from ")
        return render_template("results.html", cur=cur, area_data_form=area_data_form)