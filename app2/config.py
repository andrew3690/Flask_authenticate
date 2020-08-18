import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , login_user , logout_user , current_user , login_required 

#### Needs Mysqldb module to be installed 
app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] =  8000
app.config['SECRET KEY'] = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@:8000/flask'
app.config['DEBUG'] = True

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.loginn_view = 'login'