#!/usr/bin/python                                                         

# Import modules for CGI handling                                          
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                        
form = cgi.FieldStorage()

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

try:
    cursor.execute("SELECT * FROM flights")
    for (airline_id, flight_no, date_time, origin_id, dest_id, amt_miles) in cursor:
        print("<P>Flight: {}{}, Date: {}, Origin: {}, Destination: {}, Miles: {}</P>".format(airline_id, flight_no, date_time, origin_id, dest_id, amt_miles))
        #print(airline_id, flight_no, date_time, origin_id, dest_id, amt_miles)
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    print "<title>This Kinda Worked?...</title>"

cursor.close()
cnx.close()

print "</body>"
print "</html>"
