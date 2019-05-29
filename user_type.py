#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields - drop down menu so type will always be valid
user_type = form.getvalue('user_type')

admin        = False
airline_emp  = False
travel_agent = False
traveler     = False

if user_type == 'admin':
    admin = True
if user_type == 'airline_emp':
    airline_emp = True
if user_type == 'travel_agent':
    travel_agent = True
if user_type == 'traveler':
    traveler = True
    
#HTML header, will always print
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Working</title>"
print "</head>"
print "<body>"

if admin == True:
    print "<P>Welcome, Admin</P>"
    print "<P>Create airline: <a href='http://ada.sterncs.net/~mschick/create_airline.html'>here</a></P>"
    print "<P>Delete airline: <a href='http://ada.sterncs.net/~mschick/delete_airline.html'>here</a></P>"
if airline_emp == True:
    print "<P>Welcome, Airline Employee</P>"
    print "<P>Create flight: <a href='http://ada.sterncs.net/~mschick/create_flight.html'>here</a></P>"
    print "<P>View flights: <a href='http://ada.sterncs.net/~mschick/view_flights.html'>here</a></P>"
    print "<P>Update flights: <a href='http://ada.sterncs.net/~mschick/update_flight.html'>here</a></P>"
    print "<P>Delete flights: <a href='http://ada.sterncs.net/~mschick/delete_flight.html'>here</a></P>"

if travel_agent == True:
    print "<P>Welcome, Travel Agent</P>"
    print "<P>Create traveler: <a href='http://ada.sterncs.net/~mschick/create_traveler.html'>here</a></P>"
    print "<P>Create booking: <a href='http://ada.sterncs.net/~mschick/create_booking.html'>here</a></P>"
    print "<P>View travelers: <a href='http://ada.sterncs.net/~mschick/view_travelers.html'>here</a></P>"
    print "<P>View bookings: <a href='http://ada.sterncs.net/~mschick/view_bookings.html'>here</a></P></P>"
    print "<P>Update traveler: <a href='http://ada.sterncs.net/~mschick/update_traveler.html'>here</a></P>"
    print "<P>Delete traveler: <a href='http://ada.sterncs.net/~mschick/delete_traveler.html'>here</a></P>"
    print "<P>Delete booking: <a href='http://ada.sterncs.net/~mschick/delete_booking.html'>here</a></P>"

if traveler == True:
    print "<P>Welcome, Traveler</P>"
    print "<P>View flights: <a href='http://ada.sterncs.net/~mschick/view_flights.html'>here</a></P>"
    print "<P>View my bookings: <a href='http://ada.sterncs.net/~mschick/view_my_bookings.html'>here</a></P>"
    print "<P>View my traveler information: <a href='http://ada.sterncs.net/~mschick/view_my_traveler.html'>here</a></P>"
    print "<P>View arrivals schedule: <a href='http://ada.sterncs.net/~mschick/view_arrivals.html'>here</a></P>"
    print "<P>View departures schedule: <a href='http://ada.sterncs.net/~mschick/view_departures.html'>here</a></P>"

print "</body>"
print "</html>"
