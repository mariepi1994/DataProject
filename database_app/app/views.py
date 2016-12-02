from flask import render_template
from app import d_app
from app import mysql
from app.forms import CountrySearch


@d_app.route('/')
@d_app.route('/index')
def index():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT data from example WHERE id=1''')
	rv = cur.fetchall() #return all values 
	print rv
	return render_template('index.html')


@d_app.route('/addone/<string:insert>')
def add(insert):
	cur = mysql.connection.cursor()
	cur.execute('''SELECT MAX(ID) FROM example''')
	maxid = cur.fetchone() #this will give us a tuples
	cur.execute('''INSERT INTO example(id, data) VALUES (%s, %s)''', (maxid[0]+1, insert)) #inc the id with every insert
	mysql.connection.commit()
	return 'done'


@d_app.route('/getall')
def getall():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT * FROM example''')
	returnvals = cur.fetchall() #use fetchall because this will return more than one roll

	printthis = ""
	for i in returnvals:
		printthis += str(i) + "<br>"

	return printthis


@d_app.route('/search', methods=['GET', 'POST'])
def search():
	#info = None
	countries = ['one', 'two', 'three', 'four']
	random = 'hi'
	form = CountrySearch()
	if form.validate_on_submit():
		#countries.append(form.country_name.data)
		print countries
	return render_template('search.html', title='Search for a country',form=form, countries=countries, random=random)
