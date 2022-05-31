from flask import Flask, render_template, request, redirect
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

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        name = request.form['product_name']
        description = request.form['product_description']
        catalog = Catalog(product_name=name, product_description=description)
        db.session.add(catalog)
        db.session.commit()

    allProducts = Catalog.query.all()

    return render_template('index.html', data=allProducts)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['product_name']
        description = request.form['product_description']
        item = Catalog.query.filter_by(id=id).first()
        item.product_name = name
        item.product_description = description
        db.session.add(item)
        db.session.commit()
        return redirect('/')
        
    item = Catalog.query.filter_by(id=id).first()
    return render_template('update.html', data=item)

@app.route('/delete/<int:id>')
def delete(id):
    item = Catalog.query.filter_by(id=id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)