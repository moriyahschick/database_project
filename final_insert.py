from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='mhschick',
                              host='localhost',
                              password='moriyah',
                              database='mhschick1')
cursor = cnx.cursor()

#if you wanted to add an airport, airline, or flight after, could use these add statements
add_airport = ("INSERT INTO airports "
               "(airport_id, name, address) "
               "VALUES (%s, %s, %s)")

add_airline = ("INSERT INTO airlines "
               "(arline_id, name) "
               "VALUES (%s, %s)")

add_flight = ("INSERT INTO flight "
              "(airline_id, flight_no, date_time, origin_id, dest_id, amt_miles) "
              "VALUES (%s, %s, %s, %s, %s, %s)")

add_traveler = ("INSERT INTO travelers "
                "(traveler_id, freq_flyer_no, name, address, phone_no, nationality, passport_no) "
                "(%s, %s, %s, %s, %s, %s, %s)")


#otherwise, will load all databases with these csv's
#may not be correct data in real life but atisfactory for queries
load_airports = ("LOAD DATA LOCAL INFILE '~/dbms/airport_list.csv' "
                 "INTO TABLE airports "
                 "FIELDS TERMINATED BY ' , ' "
                 "LINES TERMINATED BY '\n' ;")


load_airlines = ("LOAD DATA LOCAL INFILE '~/dbms/airlines_list.csv' "
                 "INTO TABLE airlines "
                 "FIELDS TERMINATED BY ' , ' "
                 "LINES TERMINATED BY '\n' ;")

load_travelers = ("LOAD DATA LOCAL INFILE '~/dbms/travelers.csv' "
                  "INTO TABLE travelers "
                  "FIELDS TERMINATED BY ',' "
                  "LINES TERMINATED BY '\n' ;")

load_flights = ("LOAD DATA LOCAL INFILE '~/dbms/flights.csv' "
                "INTO TABLE flights "
                "FIELDS TERMINATED BY ',' "
                "LINES TERMINATED BY '\n' ;")

load_deptSchedule = ("LOAD DATA LOCAL INFILE '~/dbms/deptSchedule.csv' "
                     "INTO TABLE deptSchedule "
                     "FIELDS TERMINATED BY ',' "
                     "LINES TERMINATED BY '\n' ;")

load_arrivalSchedule = ("LOAD DATA LOCAL INFILE '~/dbms/arrivalSchedule.csv' "
                        "INTO TABLE arrivalSchedule "
                        "FIELDS TERMINATED BY ',' "
                        "LINES TERMINATED BY '\n' ;")

load_bookings = ("LOAD DATA LOCAL INFILE '~/dbms/bookings.csv' "
                 "INTO TABLE bookings "
                 "FIELDS TERMINATED BY ',' "
                 "LINES TERMINATED BY '\n' ;")

try:                 
    cursor.execute(load_airports)
    print("Loaded: airports")
    cursor.execute(load_airlines)
    print("Loaded: airlines")
    cursor.execute(load_travelers)
    print("Loaded: travelers")
    cursor.execute(load_flights)
    print("Loaded: flights")
    cursor.execute(load_deptSchedule)
    print("Loaded: deptSchedule")
    cursor.execute(load_arrivalSchedule)
    print("Loaded: arrivalSchedule")
    cursor.execute(load_bookings)
    print("Loaded: bookings")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_BAD_TABLE_ERROR:
    print("You've got an error: cannot load table...")
  else:
    raise

cnx.commit()

print("Committed")
cursor.close()
cnx.close()
