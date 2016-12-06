from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from app import d_app
from app import mysql
from app.forms import DBSearch
from app.forms import userLogin
from app.forms import profileChanges
from app.forms import register
from app.forms import Establishments
from app.forms import del_profile
from app.forms import ratePlace
from app.forms import changingEvents
from app.dbquery import *


@d_app.route('/')
@d_app.route('/index')
def index():
	return render_template('index.html')


@d_app.route('/login', methods=['GET', 'POST'])
def login():
	form = userLogin()
	user_info = None
	if form.validate_on_submit():
		user_name = form.username.data
		user_password = form.userpassword.data
		user_info =  get_user(user_name, user_password)
		if user_info == None:
			return redirect(url_for('login'))
		elif request.method == 'POST':
			return redirect(url_for('profile', user_vals=user_info))
	else:
		return render_template('login.html', title='Log in!',form=form, user_info=user_info)


@d_app.route('/profile/<user_vals>', methods=['GET', 'POST'])
def profile(user_vals):
	form = profileChanges()
	form2 = del_profile()
	form3 = ratePlace()
	change_fav = None

	temp = user_vals.split('+')
	userid = temp[0]
	answer = str(temp[5])
	establishments = getuser_establishment(userid)
	if form2.validate_on_submit():
		delete_user(userid)
		return redirect(url_for('deleted'))
	if form.validate_on_submit() and form.favorite.data:
		change_fav = form.favorite.data
		answer = change_favplace(user_vals, change_fav)
	if form3.validate_on_submit() and form3.est_name.data:
		place = form3.est_name.data
		rating = form3.rating.data
		user_rating(userid,place,rating)
	return render_template('profile.html', title='Welcome to your profile',form=form, form2=form2, form3=form3, temp=temp, answer=answer, establishments=establishments)

@d_app.route('/deleted', methods=['GET', 'POST'])
def deleted():
	return render_template('deleted.html', title='Goodbye!')


@d_app.route('/search', methods=['GET', 'POST'])
def search():
    form = DBSearch()
    user_search=""
    user_rating = None
    user_type = None
    user_date = None
    db_returnvals = None
    if form.validate_on_submit():
        user_search = form.search_val.data
        user_rating = form.rating.data
        user_type = form.search_type.data
        user_date = form.date.data
        db_returnvals= get_dbdata(user_search, user_rating, user_type, user_date)
    return render_template('search.html', title='Search for an Event/Establishment',form=form, db_returnvals=db_returnvals, user_search=user_search)



@d_app.route('/registration', methods=['GET', 'POST'])
def registration():
	form = register()
	username = None
	password = None
	favortieplace = None
	answer = None
	if form.validate_on_submit():
		username = form.reg_username.data
		password = form.reg_password.data
		favoriteplace = form.reg_favoriteplace.data
		answer = create_user(username, password,favoriteplace)
	return render_template('registration.html', title='Register Here!',form=form, answer=answer)

@d_app.route('/change_estabs', methods=['GET', 'POST'])
def change_estabs():
	form = Establishments()
	addordel = None
	name = None
<<<<<<< HEAD
=======
	address = None
	answer = None
	cat = None
>>>>>>> 4ec9aef05e172b3b09a58e0aa8d185925b9d0bfd
	all_places = None
	answer = None
	if form.validate_on_submit():
		addordel =  form.deloradd.data
		name = form.est_name.data
		answer = create_event(addordel, name)
		all_places = get_establishment()
	return render_template('establishments.html', title='All of the Establishments!',form=form, answer=answer, all_places = all_places)
<<<<<<< HEAD

	
@d_app.route('/change_events', methods=['GET', 'POST'])
def change_events():
	form = changingEvents()
	addordel = None
	name = None
	answer = None
	date = None
	all_events = get_events()
	if form.validate_on_submit():
		addordel =  form.deloradd.data
		name = form.event_description.data
		date = form.date.data
		answer = create_event(addordel, name) 
		all_events = get_events()
		print all_events
	return render_template('events.html', title='All of the Events!',form=form, answer=answer, all_events = all_events)
	
    
=======
>>>>>>> 4ec9aef05e172b3b09a58e0aa8d185925b9d0bfd
