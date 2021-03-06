from app import d_app
from app import mysql

def get_recommendation(UserID):
    
    print ("HEY WE MADE IT TO THE FUNCTION!!!!!!!!!!!!!!!")
    
    cur = mysql.connection.cursor()
    cur.execute('''SELECT Name, Address FROM Establishments WHERE Type = (SELECT Type FROM Establishments WHERE Establishments.EstablishmentID = (SELECT EstablishmentID FROM Users WHERE UserID = %s))''' , (str(UserID),))
    returnvals = cur.fetchall()

    print ("PRINTING RETURNVALS::::::::")
    print (returnvals)

    places = []
    for place in returnvals:
        n = str(place[0])
        a = str(place[1])
        tup = tuple((n,a))
        places.append(tup)

    print ("PRINTING RECOMMENDATIONS RIGHT BEFORE RETURN:::::::::")
    print (places)
    print ("##############################")
    return places




def get_dbdata(search, rating, utype, date):
    if utype == "Establishment":
        if search == "ALL":
            cur = mysql.connection.cursor()
            #Query for a ALL establishments
            cur.execute('''SELECT Name, Address, FLOOR(AVG(Score)) FROM EstablishmentRating, Establishments WHERE EstablishmentRating.EstablishmentID = Establishments.EstablishmentID GROUP BY EstablishmentRating.EstablishmentID''')
            returnvals = cur.fetchall() #use fetchall because this will return more than one row

            print ("PRINTING RETURNVALS::::::::")
            print (returnvals)

        else:
            
            #que = mysql.connection.cursor()
            #que.execute('''SELECT Name FROM Establishments''')
            #if search in que.fetchall():
            #    return ["THAT ESTABLISHMENT IS NOT IN OUR SYSTEM! TRY AGAIN!"]
            
            cur = mysql.connection.cursor()
            #Query for a specific Establishment
            cur.execute('''SELECT Name, Address, FLOOR(AVG(Score)) FROM EstablishmentRating, Establishments WHERE EstablishmentRating.EstablishmentID = Establishments.EstablishmentID AND Establishments.Name = %s GROUP BY EstablishmentRating.EstablishmentID ''' , (str(search),))
            returnvals = cur.fetchall() #use fetchall because this will return more than one row

            print ("PRINTING RETURNVALS::::::::")
            print (returnvals)

        places = []
        for place in returnvals:
            n = str(place[0])
            a = str(place[1])
            r = str(place[2])
            tup = tuple((n,a,r))
            places.append(tup)


    else:
        if date == "":
            cur = mysql.connection.cursor()
            #Query for ALL events without specific dates
            cur.execute('''SELECT Date, Name, Description, COUNT(UserID) FROM Events, EventRating, Establishments WHERE Events.EstablishmentID = Establishments.EstablishmentID AND Events.EventID = EventRating.EventID GROUP BY EventRating.EventID''')
            returnvals = cur.fetchall() #use fetchall because this will return more than one row
                
            print ("PRINTING RETURNVALS::::::::")
            print (returnvals)
            
        else:
            cur = mysql.connection.cursor()
            #Query for ALL events with specific dates
            cur.execute('''SELECT Date, Name, Description, COUNT(UserID) FROM Events, EventRating, Establishments WHERE Events.EstablishmentID = Establishments.EstablishmentID AND Events.EventID = EventRating.EventID AND Date = %s GROUP BY EventRating.EventID''' , (str(date),))
            returnvals = cur.fetchall() #use fetchall because this will return more than one row
                
            print ("PRINTING RETURNVALS::::::::")
            print (returnvals)
        
        places = []
        for place in returnvals:
            n = str(place[0])
            a = str(place[1])
            r = str(place[2])
	    p = str(place[3])
            tup = tuple((n,a,r,p))
            places.append(tup)

    if not returnvals:
        return ["THERE IS NO ENTRY IN OUR SYSTEM WITH THOSE SPECIFICATIONS! TRY AGAIN!"]
        """
        if search == "ALL":
            if date == "":
                cur = mysql.connection.cursor()
                #Query for ALL events without specific dates
                cur.execute('''SELECT Date, Name, Description, COUNT(UserID) FROM Events, EventRating, Establishments WHERE Events.EstablishmentID = Establishments.EstablishmentID AND Events.EventID = EventRating.EventID GROUP BY EventRating.EventID''')
                returnvals = cur.fetchall() #use fetchall because this will return more than one row

                print ("PRINTING RETURNVALS::::::::")
                print (returnvals)
            places = []
            for place in returnvals:
                n = str(place[0])
                a = str(place[1])
                r = str(place[2])
                p = str(place[3])
                tup = tuple((n,a,r,p))
                places.append(tup)

            else:
                cur = mysql.connection.cursor()
                #Query for ALL events with specific dates
                cur.execute('''SELECT Date, Name, Description, COUNT(UserID) FROM Events, EventRating, Establishments WHERE Events.EstablishmentID = Establishments.EstablishmentID AND Events.EventID = EventRating.EventID AND Date = %s GROUP BY EventRating.EventID''' , (str(date),))
                returnvals = cur.fetchall() #use fetchall because this will return more than one row

                print ("PRINTING RETURNVALS::::::::")
                print (returnvals)
            places = []
            for place in returnvals:
                n = str(place[0])
                a = str(place[1])
                r = str(place[2])
                p = str(place[3])
                tup = tuple((n,a,r,p))
                places.append(tup)

    if not returnvals:
        return ["THERE IS NO ENTRY IN OUR SYSTEM WITH THOSE SPECIFICATIONS! TRY AGAIN!"]
        
    #Format returnvals
    places = []
    for place in returnvals:
        n = str(place[0])
        a = str(place[1])
        r = str(place[2])
        tup = tuple((n,a,r))
        places.append(tup)

    print ("PRINTING PLACES RIGHT BEFORE RETURN:::::::::")
    print (places)
    print ("##############################")
            """
    return places

#validate that this is a user
#is it is a user then we find their favorite place and return it
def get_user(username, userpassword):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT * FROM Users WHERE UserName = %s and Password = %s""" , (str(username),str(userpassword),))
	returnvals = cur.fetchall() #use fetchall because this will return more than one roll


	if len(returnvals)==0:
		returnvals = None
	else:
		returnvals = get_favoriteplace(returnvals[0][0])
	return returnvals  #return a STRING of their info that includes their favorite place


def change_favplace(user_vals, changeto):
	userlist = user_vals.split('+') #gets the userid which it the first tuple
	userID = userlist[0]
	place = get_favoriteplace(userID).split('+')

	#check if the place that they want is in db
	if changeto not in get_allplaces():
		return " NOT IN THE DATABASE! TRY AGAIN.\n  Favorite: " + str(place[5])
	else: #e
		cur = mysql.connection.cursor()
		cur.execute("""SELECT EstablishmentID
						FROM  Establishments
						WHERE Name = %s""", (changeto,))
		Establishment = cur.fetchall()#graps tuple of useID BUT we need actual number
		temp = convert_tup(Establishment).split('+')
		EstablishmentID =  temp[0]
		#print EstablishmentID
		'''EstablishmentID = get_establishmentid(changeto)
		print "ESTABLISH  " + str(EstablishmentID)'''



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


#Gets the establishments that the user has rated
def getuser_establishment(userID):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT Establishments.Name, EstablishmentRating.Score
					FROM Users, Establishments, EstablishmentRating
					WHERE Establishments.EstablishmentID = EstablishmentRating.EstablishmentID AND
						  EstablishmentRating.UserID = Users.UserID AND
						  Users.UserID = %s """, (userID,))

	tup = cur.fetchall()
	places = []
	for place in tup:
		n = str(place[0])
		a = str(place[1])
		tup = tuple((n,a))
		places.append(tup)

	return places #returns string with user info AND of favorite place'''


def create_establishment(choice, name, address, category):
	if(choice == 'Add'):
		cur = mysql.connection.cursor()
		cur.execute('''SELECT MAX(EstablishmentID) FROM Establishments''')
		maxid = cur.fetchone() #this will give us a tuples
		cur.execute('''INSERT INTO Establishments(EstablishmentID, Name, Address, Type) VALUES (%s, %s, %s, %s)''', (maxid[0]+1, name, address,category))
		mysql.connection.commit()
		cur.execute('''INSERT INTO EstablishmentRating(UserID, EstablishmentID, Score) VALUES (%s, %s, %s)''', (1, maxid[0]+1, 3))
		mysql.connection.commit()
		return "Your Establishment has been created! Add more!"
	elif(choice == 'Delete'):
		cur = mysql.connection.cursor()
		if name not in get_allplaces():
			return "This establishment does not exist"
		else:
			EstablishmentID = get_establishmentid(name)
			cur.execute('''DELETE FROM Establishments WHERE Name = (%s) ''', (str(name),))
			mysql.connection.commit()
			cur.execute('''DELETE FROM EstablishmentRating WHERE EstablishmentID = (%s) ''', (EstablishmentID,))
			mysql.connection.commit()
			return "Your Establishment has been Deleted!"


def delete_user(userid):
	print "user id is: " + str(userid)
	cur = mysql.connection.cursor()
	cur.execute('''DELETE FROM Users WHERE UserID = (%s) ''', (userid,))
	mysql.connection.commit()
	#return "Your User has been Deleted!"



#gets the establishments and their rating BUT only those that have ratings
def get_est_rating():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT Establishments.Name, Establishments.Address, EstablishmentRating.Score
					FROM Establishments, EstablishmentRating
					WHERE Establishments.EstablishmentID = EstablishmentRating.EstablishmentID
					GROUP BY stablishments.Name''')
	returnvals = cur.fetchall() #use fetchall because this will return more than one roll

	places = []
	for place in returnvals:
		n = str(place[0])
		a = str(place[1])
		r =  str(place[2])
		tup = tuple((n,a,r))
		places.append(tup)

	return places

#returns a list of tuple = name,address
def get_establishment():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT Name, Address
					FROM Establishments
					''')
	returnvals = cur.fetchall() #use fetchall because this will return more than one roll

	places = []
	for place in returnvals:
		n = str(place[0])
		a = str(place[1])
		tup = tuple((n,a))
		places.append(tup)

	return places


#lets the user rate the palce
def user_rating(userid,place, rating):
	if place not in get_allplaces():
		return "Not a place!"
	else:
		EstablishmentID = get_establishmentid(place)
		print "ESTABLISH  " + str(EstablishmentID)
		cur = mysql.connection.cursor()
		cur.execute('''INSERT INTO EstablishmentRating(UserID, EstablishmentID, Score ) VALUES (%s, %s, %s)''', (userid,EstablishmentID, rating,))
		mysql.connection.commit()
		return "Your rating has been submitted!"



def create_event(choice, name, establishment):
	if(choice == 'Add'):
		EstablishmentID = get_establishmentid(establishment)
		cur = mysql.connection.cursor()
		cur.execute('''SELECT MAX(EventID) FROM Events''')
		maxid = cur.fetchone() #this will give us a tuples
		cur.execute('''INSERT INTO Events(EventID, Description, EstablishmentID) VALUES (%s, %s, %s)''', (maxid[0]+1, name,EstablishmentID))
		mysql.connection.commit()

		#### make sure juan is good ###########
		#cur.execute('''SELECT *  FROM EventRating 
		#			   WHERE EventID = %s AND UserID = %s ''', (EventID, 1))
		#val = cur.fetchone() 
		#if val is None:
		#	cur.execute('''INSERT INTO EventRating(UserID, EventID) VALUES (%s, %s)''', (1, maxid[0]+1))
		#	mysql.connection.commit()	
		
		cur.execute('''INSERT INTO EventRating(UserID, EventID) VALUES (%s, %s)''', (1, maxid[0]+1))
		mysql.connection.commit()
		return "Your Event has been created! Add more!"

	elif(choice == 'Delete'):
		cur = mysql.connection.cursor()
		if name not in get_events():
			return "This establishment does not exist"
		else:
			#EventID = get_eventid(name)
			cur.execute('''DELETE FROM Events WHERE Description = (%s) ''', (str(name),))
			mysql.connection.commit()
			#cur.execute('''DELETE FROM EstablishmentRating WHERE EstablishmentID = (%s) ''', (EstablishmentID,))
			#mysql.connection.commit()
			return "Your Establishment has been Deleted!"


def get_events():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT Description
					FROM Events
					''')
	returnvals = cur.fetchall() #use fetchall because this will return more than one roll
	places = []
	for place in returnvals:
		places.append(str(place[0]))

	return places


def user_like(userid, event):
	if event not in get_events():
		return "Not an Event!"
	else:
		EventID = get_eventid(event)
		cur = mysql.connection.cursor()
		cur.execute('''SELECT *  FROM EventRating
					   WHERE EventID = %s AND UserID = %s ''', (EventID, userid))
		val = cur.fetchone()
		if val is None:
			cur.execute('''INSERT INTO EventRating(EventID, UserID) VALUES (%s, %s)''', (EventID, userid))
			mysql.connection.commit()
			return "You liked " + str(event) + "!!"
		else:
			return "You liked " + str(event) + "!!"



def get_eventid(event):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT EventID
					FROM Events
					WHERE Description = %s """, (event,))

	tup = cur.fetchone()
	return tup[0]


def get_user_likes(userid):
	cur = mysql.connection.cursor()
	cur.execute("""SELECT Events.Description
					FROM Users, Events, EventRating
					WHERE Events.EventID = EventRating.EventID AND
						  EventRating.UserID = Users.UserID AND
						  Users.UserID = %s """, (userid,))

	tup = cur.fetchall()
	places = []
	for place in tup:
		n = str(place[0])
		places.append(n)

	return places #returns string with user info AND of favorite place'''
