import mysql.connector as mysql
from mysql.connector import errorcode

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursor = db.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.Error as err:
        print("Erreur creation database: {}".format(err))
        exit(1)

def read_database(cursor):
    cursor.execute("SHOW DATABASES")
    return

         
choix = input("Que voulez-vous faire sur les DB ? créer ou voir ")

if choix == "créer": 
    DB_NAME = input("Quel est le nom de la DB à créer ? ")       
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

elif choix == "voir":
    print("Les DB existantes sont : ")
    read_database(cursor)
    
