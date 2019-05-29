#!/usr/bin/python                                                                                                                    

# Import modules for CGI handling                                                                                                    
import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

# Create instance of FieldStorage                                                                                                    
form = cgi.FieldStorage()
old_traveler_id = form.getvalue('old_traveler_id')
new_traveler_id = form.getvalue('new_traveler_id')
new_freq_flyer_no = form.getvalue('new_freq_flyer_no')
new_name        = form.getvalue('new_name')
new_address     = form.getvalue('new_address')
new_phone_no    = form.getvalue('new_phone_no')
new_nationality = form.getvalue('new_nationality')
new_passport_no = form.getvalue('new_passport_no')


# HTML header, will always print                                                                                                     
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print "<title>Mori Schick's Database Project</title>"
print '</head>'
print '<body>'

#print "<P>%s, %s, %s, %s, %s, %s, %s, %s</P>" % (old_traveler_id, new_traveler_id, new_freq_flyer_no, new_name, new_address, new_phone_no, new_nationality, new_passport_no)

#if there are any input errors, will become true                                     
any_errors = False
#print "<P>%s</P>" % (any_errors)
#check traveler_ids  
if len(old_traveler_id) != 6:
    any_errors = True
    print "<P>The traveler ID must be of length 6</P>"

if new_traveler_id != None:
    if len(new_traveler_id) != 6:
        any_errors = True
        print "<P>The traveler ID must be of length 6</P>"
    
#check freq_flyer_no:
if new_freq_flyer_no != None:
    try:
        freq_flyer_no1 = int(new_freq_flyer_no)
    except:
        print "<P>You must enter a 4-digit number for the frequent flyer number</P>"
        any_errors = True
    if len(new_freq_flyer_no) != 4:
        any_errors = True
        print "<P>You must enter a 4-digit number for the frequent flyer number</P>"

#check name:
if new_name != None:
    if len(str(new_name)) > 25 and not all((x.isalpha() or x.isspace()) for x in new_name):
        any_errors = True
        print "<P>Names may only be letters and spaces up to length 25</P>"

#check address:
if new_address != None:
    if len(str(new_address)) > 40:
        any_errors = True
        print "<P>You must enter an address up to length 40</P>"

#check phone no:
if new_phone_no != None:
    if len(str(new_phone_no)) > 10:
        any_errors = True
        print "<P>Phone numbers must be a number up to length 10</P>"

#check nationaity:
if new_nationality != None:
    if len(str(new_nationality)) > 15:
        any_errors = True
        print "<P>Nationality may be up to length 15</P>"

#check passport:
if new_passport_no != None:
    try:
        passport_no1 = int(new_passport_no)
    except:
        any_errors = True
        print "<P>You must enter a 10-digit number for the passport number</P>"
    if len(new_passport_no) != 10:
        any_errors = True
        print "<P>You must enter a 10-digit number for the passport number</P>"

#print "<P>%s</P>" % (any_errors)
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

    
    if new_traveler_id != None:
        try:
            cursor.execute("UPDATE travelers SET traveler_id=%s WHERE traveler_id=%s", (new_traveler_id, old_traveler_id))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_freq_flyer_no != None:
        try:
            cursor.execute("UPDATE travelers SET freq_flyer_no=%s WHERE traveler_id=%s", (new_freq_flyer_no, old_traveler_id))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_name != None:
        try:
            cursor.execute("UPDATE travelers SET name=%s WHERE traveler_id=%s", (new_name, old_traveler_id))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_address != None:
        try:
            cursor.execute("UPDATE travelers SET address=%s WHERE traveler_id=%s", (new_address, old_traveler_id))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_phone_no != None:
        try:
            cursor.execute("UPDATE travelers SET phone_no=%s WHERE traveler_id=%s", (new_phone_no, old_traveler_id))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_nationality != None:
        try:
            cursor.execute("UPDATE travelers SET nationality=%s WHERE traveler_id=%s", (new_nationality, old_traveler_id))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
    if new_passport_no != NOne:
        try:
            cursor.execute("UPDATE travelers SET passport_no=%s WHERE traveler_id=%s", (new_passport_no, old_traveler_id))
            cnx.commit()
            print "<P>Update Committed</P>"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            print "<title>This Kinda Worked?...</title>"
        
    print "</body>"
    print "</html>"
