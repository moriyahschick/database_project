#!/usr/bin/python                                                      

# Import modules for CGI handling                                      
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                      
form = cgi.FieldStorage()

# Get data from fields                                                 
traveler_id   = form.getvalue('traveler_traveler_id')
freq_flyer_no = form.getvalue('traveler_freq_flyer_no')
name          = form.getvalue('traveler_name')
address       = form.getvalue('traveler_address')
phone_no      = form.getvalue('traveler_phone_no')
nationality   = form.getvalue('traveler_nationality')
passport_no   = form.getvalue('traveler_passport_no')

#must check these values to see if the user gives valid ones:
valid_traveler_id   = False
valid_freq_flyer_no = False
valid_name          = False
valid_address       = False
valid_phone_no      = False
valid_nationality   = False
valid_passport_no   = False

#HTML header, will always print
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"

#check traveler_id
if len(traveler_id) == 6:
    valid_traveler_id = True

#check freq_flyer_no:
try:
    freq_flyer_no1 = int(freq_flyer_no)
except:
    print "<P>You must enter a 4-digit number for the frequent flyer number</P>"
if int(freq_flyer_no) >= 0 and int(freq_flyer_no) < 10000:
    valid_freq_flyer_no = True

#check name:
if len(str(name)) <= 25 and all(x.isalpha() or x.isspace() for x in name):
    valid_name = True

#check address:
if len(str(address)) <= 40:
    valid_address = True

#check phone_no:
if len(str(phone_no)) <= 10:
    valid_phone_no = True

#check nationality:
if len(str(nationality)) <= 15:
    valid_nationality = True

#check passport_no:
try:
    passport_no1 = int(passport_no)
except:
    print "<P>You must enter a 10-digit number for the passport number</P>"
if int(passport_no) >= 0 and int(passport_no) < 100000000000:
    valid_passport_no = True

    
#if any are false, tell the user
if valid_traveler_id == False:
    print "<P>You have entered an invalid traveler ID:  "
    print "please enter a string of length 6 for the traveler ID</P>"

if valid_freq_flyer_no == False:
    print "<P>You have entered an invalid frequent flyer number:  "
    print "please enter a number 0-9999 for the frequent flyer number</P>"

if valid_name == False:
    print "<P>You have entered an invalid name:  "
    print "names may only be letters and spaces up to length 25</P>"

if valid_address == False:
    print "<P>You have entered an invalid address:  "
    print "please enter an address up to length 40</P>"

if valid_phone_no == False:
    print "<P>You have entered an invalid phone number:  "
    print "please enter a number up to length 10</P>"

if valid_nationality == False:
    print "<P>You have entered an invalid nationality:  "
    print "please enter a nationality up to length 15</P>"

if valid_passport_no == False:
    print "<P>You have entered an invalid passport number:  "
    print "please enter a number 0-9999999999 for the passport number</P>"

if (valid_traveler_id == False) or (valid_freq_flyer_no == False) or (valid_name == False) or (valid_address == False) or (valid_phone_no == False) or (valid_nationality == False) or (valid_passport_no == False):
    print "<P>You have one or more invalid inputs</P>"
    print "<P>Please fix these errors and try again.</P>"
    print "</body>"
    print "</html>"

#if we get here, all user given fields are valid
else:
    print "</head>"
    print "<body>"
    print "<P>Your input is valid!</P>"
    print "<h2>%s %s %s %s %s %s %s</h2>" % (traveler_id, freq_flyer_no, name, address, phone_no, nationality, passport_no)


    cnx = mysql.connector.connect(user='mhschick',
                                  host='localhost',
                                  password='moriyah',
                                  database='mhschick1')
    cursor = cnx.cursor()

    add_traveler = ("INSERT INTO travelers "
                    "(traveler_id, freq_flyer_no, name, address, phone_no, nationality, passport_no) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    data_traveler = (traveler_id, freq_flyer_no, name, address, phone_no, nationality, int(passport_no))
    
    try:
        cursor.execute(add_traveler, data_traveler)
        cnx.commit()
        print "<title>This Worked!</title>"
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print "<title>This Kinda Worked?...</title>"
        #err 1062 == primary key already in use

    cursor.close()
    cnx.close()

    print "</body>"
    print "</html>"
