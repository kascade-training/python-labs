import mysql.connector as mysql
from mysql.connector import errorcode

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursor = db.cursor()

DB_NAME = input("Quel est le nom de votre DB ? ")

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.Error as err:
        print("Erreur creation database: {}".format(err))
        exit(1)
        
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.Error as err:
    print("Database {} n'existe pas".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} a bien été créée".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)