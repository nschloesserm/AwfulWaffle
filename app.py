import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookedtables.db'

db = SQLAlchemy(app)

class BookedTables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' %self.id

bookings = []

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

    if not full_name or not email or not telephone or not date:
        error_statement = "Fields Required!"
        return render_template("booktable.html",
            error_statement=error_statement,
            full_name=full_name,
            email=email,
            telephone=telephone,
            date=date) 

    bookings.append(f"{full_name} {email} {telephone} {date} {party_size} {time} {message}")
    return render_template("admin.html", bookings=bookings)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)