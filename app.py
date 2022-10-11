import os
from flask import Flask, render_template, request, url_for, redirect, json
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime, timedelta

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    resdate = db.Column(db.String(50), nullable=False)
    partysize = db.Column(db.Integer)
    restime = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    specialmessage = db.Column(db.Text)

    def __repr__(self):
        return f'<Customer {self.fullname}>'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/booktable", methods=('GET', 'POST'))
def booktable():
    if request.method == 'POST':
        id = request.form['id']
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        resdate = request.form['resdate']
        partysize = int(request.form['partysize'])
        restime = request.form['restime']
        specialmessage = request.form['specialmessage']
        customer = Customer(id=id,
                          fullname=fullname,
                          email=email,
                          phone=phone,
                          resdate=resdate,
                          partysize=partysize,
                          restime=restime,
                          specialmessage=specialmessage)
        db.session.add(customer)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template("booktable.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/admin", methods=('GET', 'POST'))
def admin():
    customers = Customer.query.order_by(Customer.resdate or Customer.restime)
    return render_template("admin.html", customers=customers)

@app.route('/<int:customer_id>/editcustomer/', methods=('GET', 'POST'))
def edit(customer_id):
    customer = Customer.query.get_or_404(customer_id)

    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        resdate = request.form['resdate']
        partysize = int(request.form['partysize'])
        restime = request.form['restime']

        customer.fullname = fullname
        customer.email = email
        customer.phone = phone
        customer.resdate = resdate
        customer.partysize = partysize
        customer.restime = restime

        db.session.add(customer)
        db.session.commit()

        return redirect(url_for('admin'))

    return render_template('editcustomer.html', customer=customer)

@app.post('/<int:customer_id>/delete/')
def delete(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)