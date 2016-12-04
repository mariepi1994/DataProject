from app import d_app
from app import mysql

def testfunc():
	cur = mysql.connection.cursor()
	print "This needs to work"
