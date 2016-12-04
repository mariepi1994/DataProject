from app import d_app
from app import mysql

def get_dbdata(search, rating, utype, date):
	if utype == "Establishment":
		cur = mysql.connection.cursor()
		cur.execute('''SELECT * FROM example''')
		returnvals = cur.fetchall() #use fetchall because this will return more than one roll

		'''printthis = ""
		for i in returnvals:
			printthis += str(i) + "<br>"'''

		return returnvals


#validate that this is a user
#is it is a user then we find their favorite place and return it 
def get_user(username, userpassword):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT * FROM Users WHERE UserName = %s and Password = %s""" , (str(username),str(userpassword),))
	returnvals = cur.fetchall() #use fetchall because this will return more than one roll
	

	if len(returnvals)==0:
		returnvals = 'Incorrect Username or Password'
	else:
		returnvals = get_favoriteplace(returnvals[0][0])
	return returnvals  #return a STRING of their info that includes their favorite place 


def change_favplace(user_vals, changeto):
	userlist = user_vals.split('+') #gets the userid which it the first tuple
	userID = userlist[0]
	place = get_favoriteplace(userID).split('+')
	
	#check if the place that they want is in db
	if changeto not in get_allplaces():
		return " NOT IN THE DATABASW! TRY AGAIN.\n  Your favorite place is: " + str(place[5])
	else: #e
		'''cur = mysql.connection.cursor()
		cur.execute("""SELECT EstablishmentID
						FROM  Establishments
						WHERE Name = %s""", (changeto,))
		Establishment = cur.fetchall()#graps tuple of useID BUT we need actual number
		temp = convert_tup(Establishment).split('+')
		EstablishmentID =  temp[0]'''
		#print EstablishmentID
		EstablishmentID = get_establishmentid(changeto)
		print "ESTABLISH  " + str(EstablishmentID)
		


		#change the favorite place
		cur = mysql.connection.cursor()
		cur.execute("""UPDATE Users
						SET EstablishmentID = %s 
						WHERE UserID = %s """, (EstablishmentID, userID,))
		mysql.connection.commit()	

		place = get_favoriteplace(userID).split('+')
		return "Your favorite place is: " + str(changeto)
	

#returns all of the places in a list 		
def get_allplaces():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT Name FROM Establishments''')
	returnvals = cur.fetchall() #use fetchall because this will return more than one roll

	places = []
	for place in returnvals:
		places.append(str(place[0]))

	return places

#converts that weird tuple that the db return in a string "username+password+etc"
def convert_tup(tup):	
	return "+".join(map(str,list(tup[0])))	

#given the name of the place find it's establishmentID
def get_establishmentid(Name):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT EstablishmentID 
					FROM Establishments
					WHERE Name = %s """, (Name,))
	
	tup = cur.fetchone()
	return tup[0] 
	
	

#get a users favorite place
def get_favoriteplace(userID):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT * 
					FROM Users, Establishments
					WHERE Establishments.EstablishmentID = Users.EstablishmentID AND
					Users.UserID = %s """, (userID,))
	
	tup = cur.fetchall()
	returnvals = convert_tup(tup)	
	return returnvals #returns string with user info AND of favorite place


#creates user does not validate if the Establishment is correct
def create_user(username, password,favoriteplace):
	cur = mysql.connection.cursor()
	cur.execute('''SELECT MAX(UserID) FROM Users''')
	maxid = cur.fetchone() #this will give us a tuples
	EstablishmentID = get_establishmentid(favoriteplace)
	cur.execute('''INSERT INTO Users(UserID, UserName, Password, EstablishmentID ) VALUES (%s, %s, %s, %s )''', (maxid[0]+1, username, password, EstablishmentID))
	mysql.connection.commit()
	return "Your Profile has been created! GO to login to see your profile."
	
	

'''def get user_establishment(userID):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT Establishments.Name, 
					FROM Users, Establishments, EstablishmentRating
					WHERE Establishments.EstablishmentID = Users.EstablishmentID AND
						  
					Users.UserID = %s """, (userID,))
	
	tup = cur.fetchall()
	returnvals = convert_tup(tup)	
	return returnvals #returns string with user info AND of favorite place'''
	



