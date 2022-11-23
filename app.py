from flask import Flask, render_template, request

app = Flask(__name__) # Lo convierte en Flask APP

@app.route("/")
def index():
	return render_template("index.html")