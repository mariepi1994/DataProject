from flask import Flask
from flask.ext.mysqldb import MySQL

d_app = Flask(__name__)
#flask config
d_app.config['WTF_CSRF_ENABLED'] = True
d_app.config['SECRET_KEY'] = 'somesuperdupersecretkey'

#mysqldb config
d_app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
d_app.config['MYSQL_USER'] = 'sql9147252' 
d_app.config['MYSQL_PASSWORD'] = 'l3Nl6Me8sl'
d_app.config['MYSQL_DB'] = 'sql9147252'

mysql = MySQL(d_app)

#cur = mysql.connection.cursor()



from app import views

