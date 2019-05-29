#!/usr/bin/python                                                     

# Import modules for CGI handling                                    
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                    
form = cgi.FieldStorage()

# Get data from fields                                               
airline_id  = form.getvalue('flight_airline_id')
flight_no   = form.getvalue('flight_flight_no')
month       = form.getvalue('flight_month')
day         = form.getvalue('flight_day')
year        = form.getvalue('flight_year')
hour        = form.getvalue('flight_hour')
minute      = form.getvalue('flight_minute')
origin_id   = form.getvalue('flight_origin_id')
dest_id     = form.getvalue('flight_dest_id')
amt_miles   = form.getvalue('flight_amt_miles')

#must check these values to see if the user gives valid ones:
valid_flight_no = False
valid_year      = False
valid_hour      = False
valid_minute    = False
valid_amt_miles = False
valid_airports  = False

#HTML header, will always print
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"

#check flight_no:
try:
    flight_no1 = int(flight_no)
except:
    print "<P>You must enter a number 00000-99999 for the flight no</P>"
if int(flight_no) >= 0 and int(flight_no) < 100000:
    valid_flight_no = True

#check year:
try:
    year1 = int(year)
except:
    print "<P>You must enter a year 1960-2019 for the year</P>"
if int(year) > 1959 and int(year) < 2020:
    valid_year = True

#check hour:
try:
    hour1 = int(hour)
except:
    print "<P>You must enter a number 0-23 for the hour</P>"
if int(hour) >= 0 and int(hour) < 24:
    valid_hour = True
    
#check minute:
try:
    minute1 = int(minute)
except:
    print "<P>You must enter a number 0-59 for the minute</P>"
if int(minute) >= 0 and int(minute) < 60:
    valid_minute = True

#check amt_miles:    
try:
    amt_miles1 = int(amt_miles)
except:
    print "<P>You must enter a number 0-999999 for the amount of miles</P>"
if int(amt_miles) >= 0 and int(amt_miles) < 1000000:
    valid_amt_miles = True

if origin_id != dest_id:
    valid_airports = True

#if any are false, tell the user
if valid_flight_no == False:
    print "<P>You have entered an invalid flight number:  "
    print "please enter a number 00000-99999 for the flight no</P>"

if valid_year == False:
    print "<P>You have entered an invalid year:  "
    print "please enter a year 1960-2019 for the year</P>"

if valid_hour == False:
    print "<P>You have entered an invalid hour:  "
    print "please enter a number 0-23 for the hour</P>"

if valid_minute == False:
    print "<P>You have entered an invalid minute:  "
    print "please enter a number 0-59 for the minute</P>"

if valid_amt_miles == False:
    print "<P>You have entered an invalid amount of miles:  "
    print "please enter a number 0-999999 for the amount of miles</P>"

if (valid_flight_no == False) or (valid_year == False) or (valid_hour == False) or (valid_minute == False) or (valid_amt_miles == False):
    print "<P>You have one or more invalid inputs</P>"
    print "<P>Please fix these errors and try again.</P>"
    print "</body>"
    print "</html>" 


#if we get here, all user given fields are valid
else:
    if int(hour) < 10:
        hour = "0" + str(hour)
    if int(minute) < 10:
        minute = "0" + str(minute)
        
    date_time = str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":00"
           
    print "</head>"
    print "<body>"
    print "<P>Your input is valid!</P>"
    print "<h2>Your flight is: %s %s %s %s %s %s %s %s %s %s %s</h2>" % (airline_id, flight_no, month, day, year, hour, minute, origin_id, dest_id, amt_miles, date_time)
    
    
    cnx = mysql.connector.connect(user='mhschick',
                                  host='localhost',
                                  password='moriyah',
                                  database='mhschick1')
    cursor = cnx.cursor()

    add_flight = ("INSERT INTO flights "
                  "(airline_id, flight_no, date_time, origin_id, dest_id, amt_miles) "
                  "VALUES (%s, %s, %s, %s, %s, %s)")
    
    data_flight = (airline_id, int(flight_no), date_time, origin_id, dest_id, int(amt_miles))
    
    add_deptSchedule = ("INSERT INTO deptSchedule "
                        "(airport_id, airline_id, flight_no, date_time) "
                        "VALUES (%s, %s, %s, %s)")
    
    data_deptSchedule = (origin_id, airline_id, int(flight_no), date_time)

    add_arrivalSchedule = ("INSERT INTO arrivalSchedule "
                           "(airport_id, airline_id, flight_no, date_time) "
                           "VALUES (%s, %s, %s, %s)")
    
    data_arrivalSchedule = (dest_id, airline_id, int(flight_no), date_time)
    
    try:
        cursor.execute(add_flight, data_flight)
        cursor.execute(add_deptSchedule, data_deptSchedule)
        cursor.execute(add_arrivalSchedule, data_arrivalSchedule)
        cnx.commit()
        print "<title>This Worked!</title>"
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print "<title>This Kinda Worked?...</title>"
        
    cursor.close()
    cnx.close()
    
    print "</body>"
    print "</html>"
