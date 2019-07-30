from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# Database
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/flask'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO'] = True

# app.config['SQLALCHEMY_BINDS'] = {'mysqldb': 'mysql+pymysql://root:root@localhost:3306/product''}
# SQLALCHEMY_BINDS = {'mysqldb': 'mysql://root:root@localhost/product'}

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)