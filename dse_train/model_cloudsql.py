# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import pymysql
import pymysql.cursors
import config


builtin_list = list


db = SQLAlchemy()


def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data


# # [START model]
# class Book(db.Model):
#     __tablename__ = 'books2'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))
#     author = db.Column(db.String(255))
#     publishedDate = db.Column(db.String(255))
#     imageUrl = db.Column(db.String(255))
#     description = db.Column(db.String(4096))
#     createdBy = db.Column(db.String(255))
#     createdById = db.Column(db.String(255))

#     def __repr__(self):
#         return "<Book(title='%s', author=%s)" % (self.title, self.author)
# # [END model]

# [START model]
class diabetes(db.Model):
    __tablename__ = 'diabetes'

    # preg = db.Column(db.String(10), primary_key=True)
    # plas = db.Column(db.String(10), primary_key=True)
    # pres = db.Column(db.String(10), primary_key=True)
    # skin = db.Column(db.String(10), primary_key=True)
    # test = db.Column(db.String(10), primary_key=True)
    # mass = db.Column(db.String(10), primary_key=True)
    # pedi = db.Column(db.String(10), primary_key=True)
    # age = db.Column(db.String(10), primary_key=True)
    # Class = db.Column(db.String(10), primary_key=True)
    __table_args__ = tuple(UniqueConstraint('preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'Class', name='_rowid_1_uc'))
    rowid = db.Column(db.Integer, primary_key=True)
    preg = db.Column(db.String(10))
    plas = db.Column(db.String(10))
    pres = db.Column(db.String(10))
    skin = db.Column(db.String(10))
    test = db.Column(db.String(10))
    mass = db.Column(db.String(10))
    pedi = db.Column(db.String(10))
    age = db.Column(db.String(10))
    Class = db.Column(db.String(10))
    

    def __repr__(self):
        return '<diabetes %r>' % (self.preg)
# [END model]

#[START list]
def list(limit=10, cursor=None):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    init_app(app)
    
    cursor = int(cursor) if cursor else 0
    with app.app_context():
        query = db.Query(diabetes.query.all())
    #data = builtin_list(map(from_sql, query.all()))
   # next_page = cursor + limit if len(books) == limit else None
    return (query)
#[END list]


#[START list]
def getdata(min_age, max_age):
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    init_app(app)
    
    with app.app_context():
        # query = diabetes.query.all()
        query = diabetes.query.filter(diabetes.age >= min_age, diabetes.age <= max_age).all()
    return (query)
#[END list]

# # [START read]
# def read(id):
#     result = Book.query.get(id)
#     if not result:
#         return None
#     return from_sql(result)
# # [END read]


# [START create]
def create(data):
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    init_app(app)
        # from app import diabetes
    
    # 
    with app.app_context():
        for index, row in data.iterrows():
            diabetes_insert = diabetes(preg= row[0], plas =row[1], pres =row[2], skin =row[3], test =row[4], mass =row[5], pedi =row[6][:10], age =row[7], Class =row[8])
        #datasql = data.to_sql(name='diabetes', con=db.engine, index=False)
        
            db.session.add(diabetes_insert)
            db.session.commit()
    return 'done'
# [END create]


# # [START update]
# def update(data, id):
#     book = Book.query.get(id)
#     for k, v in data.items():
#         setattr(book, k, v)
#     db.session.commit()
#     return from_sql(book)
# # [END update]


# def delete(id):
#     Book.query.filter_by(id=id).delete()
#     db.session.commit()
# def connect_to_db():
#     connection = pymysql.connect(host='104.198.16.131',
#                              user='root',
#                              password='BI4ever.1',
#                              db='dse',
#                              charset='ASCII',
#                              cursorclass=pymysql.cursors.DictCursor)
#     return connection


def _create_database():
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print("All tables created")


if __name__ == '__main__':
    _create_database()
