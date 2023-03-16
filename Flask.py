from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import  Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sql_user:sql_password@localhost/dbparty'
db = SQLAlchemy(app)


class Visitor(db.Model):
    id = db.Column('visitor_id', Integer, primary_key=True)
    name = Column(String)


def __init__(self, name):
    self.name = name


with app.app_context():
    db.create_all()


@app.route("/visitor/<string:name>")
def add_visitor(name):
    user = Visitor.query.filter_by(name=name).first()
    if user:
        return f'{name} is already exists!'
    visitor = Visitor(name=name)
    db.session.add(visitor)
    db.session.commit()
    return 'Done'
