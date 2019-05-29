#!/usr/bin/python                                                                                                                   

# Import modules for CGI handling                                                                                                    
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                                                                                    
form = cgi.FieldStorage()

# Get data from form
airport_id = form.getvalue('airport_id')
name       = form.getvalue('airport_name')
address    = form.getvalue('airport_address')

#HTML header, will always print                                                                                                      
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
#print "<P>%s, %s, %s</P>" % (airport_id, name, address)

valid_id      = False
valid_name    = False
valid_address = False

# check input                                                                                                                        
if len(airport_id) == 3:
    valid_id = True
    airport_id = airport_id.upper()
if (len(name) >= 1) and (len(name) <= 40) and all(x.isalpha() or x.isspace() for x in name):
    valid_name = True
if len(address) >= 1 and len(address) <= 40:
    valid_address = True

#if any are false, tell the user                                                                                                           
if valid_id == False:
    print "<P>You have entered an invalid airport ID:  "
    print "please enter a string of length 3 for the airport ID</P>"
if valid_name == False:
    print "<P>You have entered an invalid airport name:  "
    print "names may only be letters and spaces up to length 40</P>"
if valid_address == False:
    print "<P>You have entered an invalid airport address:  "
    print "names may only be up to length 40</P>"
if (valid_id == False) or (valid_name == False) or (valid_address == False):
    print "<P>You have one or more invalid inputs</P>"
    print "<P>Please fix these errors and try again.</P>"
    print "</body>"
    print "</html>"

else:
    print "</head>"
    print "<body>"
    print "<P>Got here</P>"

    cnx = mysql.connector.connect(user='mhschick',
                                  host='localhost',
                                  password='moriyah',
                                  database='mhschick1')
    cursor = cnx.cursor()

    add_airport = ("INSERT INTO airports "
                   "(airline_id, name, address) "
                   "VALUES (%s, %s, %s)")

    data_airport = (airline_id, name, address,)

    try:
        cursor.execute(add_airport, (data_airport))
        cnx.commit()
        print "<title>This Worked!</title>"
        print "<P>You have created Airport %s %s, %s<P>" % (airport_id, name, address)
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print "<title>This Kinda Worked?...</title>"

    cursor.close()
    cnx.close()

    print "</body>"
    print "</html>"
