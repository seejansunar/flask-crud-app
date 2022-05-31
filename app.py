from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import true

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///catalog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), nullable=False)
    product_description = db.Column(db.String(500), nullable=False)
    added_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.product_name}"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/add_product')
def add_product():
    catalog = Catalog(product_name="Lenovo G50-80", product_description="My first product")
    db.session.add(catalog)
    db.session.commit()
    allProducts = Catalog.query.all()

    return render_template('index.html', data=allProducts)

@app.route('/show')
def products():
    allProducts = Catalog.query.all()
    print(allProducts)
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)