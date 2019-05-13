from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

DB_NAME = 'mhschick1'

TABLES = {}

TABLES['airlines'] = (
    "CREATE TABLE `airlines` ("
    "  `airline_id`   varchar(6)    NOT NULL  ,"
    "  `name`         varchar(25)   NOT NULL  ,"
    "  PRIMARY KEY (`airline_id`), UNIQUE KEY `airline_id` (`airline_id`)"
    ") ENGINE=InnoDB")

TABLES['airports'] = (
    "CREATE TABLE `airports` ("                             
    "  `airport_id`  char(3)       NOT NULL,"
    "  `name`        varchar(40)   NOT NULL,"
    "  `addresss`    varchar(40)   NOT NULL,"
    "  PRIMARY KEY (`airport_id`), UNIQUE KEY `airport_id` (`airport_id`)"
    ") ENGINE=InnoDB")

TABLES['flights'] = (
    "CREATE TABLE `flights` ("
    "  `airline_id` char(2)       NOT NULL,                  " 
    "  `flight_no`  int(5)        NOT NULL,                  "
    "  `date_time`  timestamp(6)  NOT NULL,                  "               
    "  `origin_id`  char(3)       NOT NULL,                  "               
    "  `dest_id`    char(3)       NOT NULL,                  "             
    "  `amt_miles`  int(6)        NOT NULL,                  "
    "  PRIMARY KEY (`airline_id`, `flight_no`),"                       
    "  KEY `flight_no` (`flight_no`),"
    "  CONSTRAINT `airline` FOREIGN KEY (`airline_id`) "
    "     REFERENCES `airlines` (`airline_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `airport_origin` FOREIGN KEY (`origin_id`) "
    "     REFERENCES `airports` (`airport_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `airport_dest` FOREIGN KEY (`dest_id`) "
    "     REFERENCES `airports` (`airport_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['travelers'] = (
    "CREATE TABLE `travelers` ("
    "  `traveler_id`     char(6)      NOT NULL                 ,"
    "  `freq_flyer_no`   char(4)                               ,"
    "  `name`            varchar(25)  NOT NULL                 ,"
    "  `address`         varchar(40)  NOT NULL                 ,"
    "  `phone_no`        varchar(10)  NOT NULL                 ,"
    "  `nationality`     varchar(15)  NOT NULL                 ,"
    "  `passport_no`     int(10)      NOT NULL                 ,"
    "  PRIMARY KEY (`traveler_id`),"
    "  KEY `passport_no` (`passport_no`)"
    "  ) ENGINE=InnoDB")

TABLES['deptSchedule'] = (
    "CREATE TABLE `deptSchedule` ("
    "  `airport_id` char(3)         NOT NULL,"
    "  `airline_id` char(2)         NOT NULL,"
    "  `flight_no`  int(5)          NOT NULL,"
    "  `date_time`  timestamp(6)    NOT NULL,"
    "  PRIMARY KEY (`airline_id`, `flight_no`),"
    "  CONSTRAINT `dept_airport1` FOREIGN KEY (`airport_id`) "
    "     REFERENCES `flights` (`origin_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `airline_foreign1` FOREIGN KEY (`airline_id`) "
    "     REFERENCES `airlines` (`airline_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `flight_foreign1` FOREIGN KEY (`flight_no`) "
    "     REFERENCES `flights` (`flight_no`) ON DELETE CASCADE"
    "  ) ENGINE=InnoDB")

TABLES['arrivalSchedule'] = (
    "CREATE TABLE `arrivalSchedule` ("
    "  `airport_id` char(3)        NOT NULL,"
    "  `airline_id` char(2)        NOT NULL,"
    "  `flight_no`  int(5)         NOT NULL,"
    "  `date_time`  timestamp(6)   NOT NULL,"
    "  PRIMARY KEY (`airline_id`, `flight_no`),"
    "  CONSTRAINT `dept_airport2` FOREIGN KEY (`airport_id`) "
    "     REFERENCES `flights` (`dest_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `airline_foreign2` FOREIGN KEY (`airline_id`) "
    "     REFERENCES `airlines` (`airline_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `flight_foreign2` FOREIGN KEY (`flight_no`) "
    "     REFERENCES `flights` (`flight_no`) ON DELETE CASCADE"
    "  ) ENGINE=InnoDB")

TABLES['bookings'] = (
    "CREATE TABLE `bookings` ("
    "  `traveler_id` char(6)       NOT NULL,"
    "  `seat`        varchar(3)    NOT NULL,"
    "  `airline_id`  char(2)       NOT NULL,"
    "  `flight_no`   int(5)        NOT NULL,"
    "  PRIMARY KEY (`traveler_id`, `airline_id`, `flight_no`),"
    "  CONSTRAINT `booking_traveler_id` FOREIGN KEY (`traveler_id`) "
    "    REFERENCES `travelers` (`traveler_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_airline_id` FOREIGN KEY (`airline_id`) "
    "    REFERENCES `flights` (`airline_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `booking_flight_no` FOREIGN KEY (`flight_no`)"
    "    REFERENCES `flights` (`flight_no`) ON DELETE CASCADE"
    "  ) ENGINE=InnoDB")
    

##############################################


cnx = mysql.connector.connect(user='mhschick', password='moriyah', host='localhost')
cursor = cnx.cursor()
    
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
        
try:
  cursor.execute("DROP TABLE IF EXISTS arrivalSchedule")
  cursor.execute("DROP TABLE IF EXISTS deptSchedule")
  cursor.execute("DROP TABLE IF EXISTS bookings")
  cursor.execute("DROP TABLE IF EXISTS travelers")
  cursor.execute("DROP TABLE IF EXISTS flights")
  cursor.execute("DROP TABLE IF EXISTS airlines")
  cursor.execute("DROP TABLE IF EXISTS airports")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_BAD_TABLE_ERROR:
    print("You've got an error: cannot drop table...")
  else:
    raise
        
for table_name in TABLES:
    
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
        

cursor.close()
cnx.close()
