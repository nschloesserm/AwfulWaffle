

import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/booktable")
def booktable():
    return render_template("booktable.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/admin", methods=["POST"])
def admin():
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    telephone = request.form.get("telephone")
    date = request.form.get("date")
    party_size = request.form.get("party_size")
    time = request.form.get("time")
    message = request.form.get("message")
    return render_template("admin.html", full_name=full_name, email=email, telephone=telephone, date=date, party_size=party_size, time=time, message=message)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)