#!/usr/bin/python                                                      

# Import modules for CGI handling                                      
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                      
form = cgi.FieldStorage()
old_airline_id = form.getvalue('old_airline_id')
old_flight_no  = form.getvalue('old_flight_no')
new_airline_id = form.getvalue('new_airline_id')
new_flight_no  = form.getvalue('new_flight_no')
new_month      = form.getvalue('new_month')
new_day        = form.getvalue('new_day')
new_year       = form.getvalue('new_year')
new_hour       = form.getvalue('new_hour')
new_minute     = form.getvalue('new_minute')
new_origin_id  = form.getvalue('new_origin_id')
new_dest_id    = form.getvalue('new_dest_id')
new_amt_miles  = form.getvalue('new_amt_miles')

# HTML header, will always print                                        
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print "<title>Mori Schick's Database Project</title>"
print '</head>'
print '<body>'

if new_airline_id == "None":
    new_airline_id = None
if new_month == "None":
    new_month = None
if new_day == "None":
    new_day = None
if new_origin_id == "None":
    new_origin_id = None
if new_dest_id == "None":
    new_dest_id = None
    
#if there are any input errors, will become true
any_errors = False

# check original flight_no:   (must always be given) 
try:
    flight_no1 = int(old_flight_no)
except:
    print "<P>You must enter a number 00000-99999 for the original flight no</P>"
    any_errors = True

# only validate other values (that would normally be validated)
# if they are given
try:
    if new_flight_no != None:
        flight_no1 = int(new_flight_no)
except:
    print "<P>You must enter a number 00000-99999 for the new flight no</P>"
    any_errors = True
try:
    if new_year != None:
        year1 = int(new_year)
except:
    print "<P>You must enter a year 1960-2019 for the year</P>"
    any_errors = True
try:
    if new_hour != None:
        hour1 = int(hour)
except:
    print "<P>You must enter a number 0-23 for the hour</P>"
    any_errors = True
try:
    if new_minute != None:
        minute1 = int(minute)
except:
    print "<P>You must enter a number 0-59 for the minute</P>"
    any_errors = True
try:
    if new_amt_miles != None:
        amt_miles1 = int(amt_miles)
except:
    print "<P>You must enter a number 0-999999 for the amount of miles</P>"
    any_errors = True
if (new_origin_id == new_dest_id) and (new_origin_id != None):
    any_errors = True
# all new date_time must be given
new_date_time = None
if (new_month != None) and (new_day != None) and (new_year != None) and (new_hour != None) and (new_inute != None):
    if int(new_hour) < 10:
        new_hour = "0" + str(new_hour)
    if int(new_minute) < 10:
        new_minute = "0" + str(new_minute)

    new_date_time = str(new_year) + "-" + str(new_month) + "-" + str(new_day) + " " + str(new_hour) + ":" + str(new_minute) + ":00"
 
if any_errors == True:
    print "<P>Please resolve above errors.</P>"
    print "</body>"
    print "</html>"

else:
    cnx = mysql.connector.connect(user='mhschick',
                                  host='localhost',
                                  password='moriyah',
                                  database='mhschick1')
    cursor = cnx.cursor()
    if new_airline_id != None:
        try:
            cursor.execute("UPDATE flights SET airline_id=%s WHERE airline_id=%s AND flight_no=%s", (new_airline_id, old_airline_id, old_flight_no))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_flight_no != None:
        try:
            cursor.execute("UPDATE flights SET flight_no=%s WHERE airline_id=%s AND flight_no=%s", (new_flight_no, old_airline_id, old_flight_no))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_date_time != None:
        try:
            cursor.execute("UPDATE flights SET date_time=%s WHERE airline_id=%s AND flight_no=%s", (new_date_time, old_airline_id, old_flight_no))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_origin_id != None:
        try:
            cursor.execute("UPDATE flights SET origin_id=%s WHERE airline_id=%s AND flight_no=%s", (new_origin_id, old_airline_id, old_flight_no))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_dest_id != None:
        try:
            cursor.execute("UPDATE flights SET dest_id=%s WHERE airline_id=%s AND flight_no=%s", (new_dest_id, old_airline_id, old_flight_no))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_amt_miles != None:
        try:
            cursor.execute("UPDATE flights SET amt_miles=%s WHERE airline_id=%s AND flight_no=%s", (amt_miles, old_airline_id, old_flight_no))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"

    print "</body>"
    print "</html>"
