#!/usr/bin/python                                                                

# Import modules for CGI handling                                              
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                                
form = cgi.FieldStorage()
airline_id = form.getvalue('delete_airline_id')
flight_no  = form.getvalue('delete_flight_no')

#HTML header, will always print                                                                                        
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print "<title>Mori Schick's Database Project</title>"
print '</head>'
print '<body>'

#print "<P>%s, %s</P>" % (airline_id, flight_no)

# no need to validate flight_no, if the user inputs an invalid flight_no
# no flight will be found and nothing will be deleted

cnx = mysql.connector.connect(user='mhschick',
                              host='localhost',
                              password='moriyah',
                              database='mhschick1')

cursor = cnx.cursor()

try:
    cursor.execute("DELETE FROM flights WHERE airline_id=%s AND flight_no=%s", (airline_id, flight_no))
    cnx.commit()
    print "<P>You have deleted Flight: %s %s</P>" % (airline_id, flight_no)
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
    print "<title>This Kinda Worked?...</title>"

cursor.close()
cnx.close()

print "</body>"
print "</html>"
