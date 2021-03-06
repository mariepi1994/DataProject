from flask_wtf import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import RadioField
from wtforms.validators import DataRequired
from wtforms.validators import optional
#from app import d_app
#from app import mysql
from app.dbquery import get_allplaces
#from app.dbquery import *
from app.test import *




class DBSearch(Form):
    #places2 = get_allplaces()
    search_val = StringField('search_val', validators=[optional()])
    date = StringField('date', validators=[optional()])
    rating = SelectField('rating', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators = [optional()])
    search_type = SelectField('search_type', choices = [('Event', 'Event'), ('Establishment', 'Establishment')], validators = [DataRequired()])

class userLogin(Form):
    username = StringField('username', validators=[DataRequired()])
    userpassword = StringField('usepassword', validators=[DataRequired()])

class profileChanges(Form):
	favorite = StringField('favorite', validators=[optional()])

class likeEvent(Form):
	like = StringField('like', validators=[optional()])

class del_profile(Form):
	button = RadioField('button', choices=[('Delete','Check to delete')])

class register(Form):
	reg_username = StringField('reg_username', validators=[DataRequired()])
	reg_password = StringField('reg_password', validators=[DataRequired()])
	reg_favoriteplace =  StringField('reg_favoriteplace', validators=[optional()])

class Establishments(Form):
	deloradd = SelectField('deloradd', choices=[('Delete', 'Delete'), ('Add', 'Add')], validators = [DataRequired()])
	est_name = StringField('est_name', validators=[DataRequired()])
	est_address = StringField('est_address', validators=[optional()])
	food = [('American', 'American'), ('Pizza', 'Pizza'), ('SandwichesAndWraps','SandwichesAndWraps'), ('Asian','Asian'), ('Sweets','Sweets'), ('Breakfast','Breakfast')]
	est_category = SelectField('est_category', choices = food, validators = [DataRequired()])


class ratePlace(Form):
	est_name = StringField('est_name', validators=[DataRequired()])
	rating = SelectField('rating', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators = [DataRequired()])


class changingEvents(Form):
	deloradd = SelectField('deloradd', choices=[('Delete', 'Delete'), ('Add', 'Add')], validators = [DataRequired()])
	event_description = StringField('event_description', validators=[DataRequired()])
	est_name = StringField('est_name', validators=[optional()])
	date = StringField('date', validators=[optional()])
	
