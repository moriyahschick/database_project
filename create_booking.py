#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
traveler_id = form.getvalue('booking_traveler_id')
seat_no     = form.getvalue('booking_seat_no')
seat_letter = form.getvalue('booking_seat_letter')
airline_id  = form.getvalue('booking_airline_id')
flight_no   = form.getvalue('booking_flight_no')

#must check these values to see if the user gives valid types:
valid_traveler_id = False
valid_flight_no   = False

#HTML header, will always print
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"

#check traveler_id:
if len(traveler_id) == 6:
    valid_traveler_id = True

#check flight_no:
try:
    flight_no1 = int(flight_no)
except:
    print "<P>You must enter a number 00000-99999 for the flight no</P>"
if int(flight_no) >= 0 and int(flight_no) < 100000:
    valid_flight_no = True

#if any are false, tell the user:
if valid_traveler_id == False:
    print "<P>You have entered an invalid traveler ID:  "
    print "please enter a string of length 6 for the traveler ID</P>"

if valid_flight_no == False:
    print "<P>You have entered an invalid flight number:  "
    print "please enter a number 00000-99999 for the flight no</P>"

if (valid_traveler_id == False) or (valid_flight_no == False):
    print "<P>You have one or more invalid inputs</P>"
    print "<P>Please fix these errors and try again.</P>"
    print "</body>" #??
    print "</html>" #?? maybe should get rid of these two

#if we get here, all user given fields are valid                               
else:
    seat = str(seat_no) + str(seat_letter)
    
    print "</head>"
    print "<body>"
    print "<P>Your input is valid!</P>"
    print "<h2>You have created a booking for: %s %s %s %s %s</h2>" % (traveler_id, seat_no, seat_letter, airline_id, flight_no)

    cnx = mysql.connector.connect(user='mhschick',
                                  host='localhost',
                                  password='moriyah',
                                  database='mhschick1')
    cursor = cnx.cursor()

    add_booking = ("INSERT INTO bookings "
                   "(traveler_id, seat, airline_id, flight_no) "
                   "VALUES (%s, %s, %s, %s)")

    data_booking = (traveler_id, seat, airline_id, int(flight_no))

    #check foreign key constraints
    try:
        check_flight = ("SELECT * "
                        "FROM flights "
                        "WHERE airline_id=%s AND flight_no=%s")
        cursor.execute(check_flight, (airline_id, flight_no))
        rows = cursor.fetchall()
        if rows is None:
            print "<P>This flight does not exist, so you cannot make a booking for it.</P>"
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print "<title>This Kinda Worked?...</title>"

    try:
        cursor.execute(add_booking, data_booking)
        cnx.commit()
        print "<title>This Worked!</title>"
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print "<title>This Kinda Worked?...</title>"

    cursor.close()
    cnx.close()

    print "</body>"
    print "</html>"
