import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/bookedtables.db'

db = SQLAlchemy(app)


class Bookedtables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.id


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

@app.route("/admin", methods=["POST","GET"])
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
        return render_template("booktable.html", error_statement= error_statement, full_name=full_name, email=email, telephone=telephone, date=date) 

    if request.method == "POST":
        cust_name = request.form['full_name']
        new_cust = Bookedtables(name=cust_name)

        try:
            db.session.add(new_cust)
            db.session.commit()
            return redirect('/booktable')
            
        except:
            return "there was an error"
    else:
        customers = Bookedtables.query
        return render_template("admin.html", customers=customers)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)