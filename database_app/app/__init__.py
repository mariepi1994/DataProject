from flask import Flask
from flask.ext.mysqldb import MySQL
#from flask_sqlalchemy import SQLAlchemy

d_app = Flask(__name__)
#flask config
d_app.config['WTF_CSRF_ENABLED'] = True
d_app.config['SECRET_KEY'] = 'somesuperdupersecretkey'


#d_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql9147252:l3Nl6Me8sl@sql9.freemysqlhosting.net/sql9147252'
#d_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#d_app.config.from_object('config')

#mysqldb config
d_app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
d_app.config['MYSQL_USER'] = 'sql9147252' 
d_app.config['MYSQL_PASSWORD'] = 'l3Nl6Me8sl'
d_app.config['MYSQL_DB'] = 'sql9147252'
mysql = MySQL(d_app)



"""db = SQLAlchemy(d_app)
class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))"""

from app import views

