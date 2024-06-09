import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='$Unny2092', database='gs')

  return __cnx

# import mysql.connector

# cnx = mysql.connector.connect(user='root', password='$Unny2092',
#                               host='127.0.0.1',
#                               database='gs')
# cnx.close()