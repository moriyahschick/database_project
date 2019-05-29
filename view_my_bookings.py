#!/usr/bin/python                                                

# Import modules for CGI handling                                
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage
form = cgi.FieldStorage()
traveler_id = form.getvalue('traveler_id')

#HTML header, will always print
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print "<title>Mori Schick's Database Project</title>"
print '</head>'
print '<body>'

cnx = mysql.connector.connect(user='mhschick',
                              host='localhost',
                              password='moriyah',
                              database='mhschick1')

cursor = cnx.cursor()

if len(traveler_id) != 6:
    print "<P>Traveler ID must be of length 6.</P>"

else:
    try:
        cursor.execute("SELECT * FROM bookings WHERE traveler_id = %s", (traveler_id,))
        for (traveler_id, seat, airline_id, flight_no) in cursor:
            print("<P>Traveler ID: {}, Flight: {}{}, Seat: {}</P>".format(traveler_id, airline_id, flight_no, seat))
        print "<P>End of Bookings Found</P>"
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print "<title>This Kinda Worked?...</title>"
    
cursor.close()
cnx.close()

print "</body>"
print "</html>"
