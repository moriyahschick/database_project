#!/usr/bin/python                                                                                                                   

# Import modules for CGI handling                                                                                                  
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                                                                                  
form = cgi.FieldStorage()

# Get data from fields
airline_id   = form.getvalue('airline_id')
airline_name = form.getvalue('airline_name')

valid_id   = False
valid_name = False

#HTML header, will always print                                                                                                   
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"

# check input
if len(airline_id) == 2:
    valid_id = True
    airline_id = airline_id.upper()

if len(str(airline_name)) <= 25 and all(x.isalpha() or x.isspace() for x in airline_name):
    valid_name = True

#if any are false, tell the user                                                                                                     
if valid_id == False:
    print "<P>You have entered an invalid airline ID:  "
    print "please enter a string of length 2 for the airline ID</P>"

if valid_name == False:
    print "<P>You have entered an invalid airline name:  "
    print "names may only be letters and spaces up to length 25</P>"

if (valid_id == False) or (valid_name == False):
    print "<P>You have one or more invalid inputs</P>"
    print "<P>Please fix these errors and try again.</P>"
    print "</body>"
    print "</html>"

else:
    print "</head>"
    print "<body>"

    cnx = mysql.connector.connect(user='mhschick',
                                  host='localhost',
                                  password='moriyah',
                                  database='mhschick1')
    cursor = cnx.cursor()

    add_airline = ("INSERT INTO airlines "
                   "(airline_id, name) "
                   "VALUES (%s, %s)")
    
    data_airline = (airline_id, airline_name)

    try:
        cursor.execute(add_airline, data_airline)
        cnx.commit()
        print "<title>This Worked!</title>"
        print "<P>You have created Airline %s %s<P>" % (airline_id, airline_name)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print "<title>This Kinda Worked?...</title>"

    cursor.close()
    cnx.close()
        
    print "</body>"
    print "</html>"
