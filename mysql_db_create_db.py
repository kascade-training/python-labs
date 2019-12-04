import mysql.connector
from mysql.connector import errorcode # on obtient les messages d'erreurs systèmes

# en définissant une configuration MySql config, config1, config2 ... on peut dans le même script se connecter simultanément à plusieurs bases de données.  
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost'
}

cnx = mysql.connector.connect(**config) # on se connecte à la base de données définie dans config
cursor = cnx.cursor() 

DB_NAME = 'm2i_python_db'


TABLES = {}

TABLES ['Espece'] = ("CREATE TABLE Espece (id smallint(6) unsigned NOT NULL AUTO_INCREMENT,  nom_courant varchar(40) NOT NULL,  nom_latin varchar(40) NOT NULL,  description text,  PRIMARY KEY (id), UNIQUE KEY nom_latin (nom_latin)) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;")
TABLES ['Animal'] = ("CREATE TABLE Animal (id smallint(6) unsigned NOT NULL AUTO_INCREMENT,  sexe char(1) DEFAULT NULL, date_naissance datetime NOT NULL, nom varchar(30) DEFAULT NULL,  commentaires text, espece_id smallint(6) unsigned NOT NULL,  race_id smallint(6) unsigned DEFAULT NULL,  mere_id smallint(6) unsigned DEFAULT NULL,pere_id smallint(6) unsigned DEFAULT NULL, PRIMARY KEY (id), UNIQUE KEY ind_uni_nom_espece_id (nom,espece_id)) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;")
TABLES ['Race'] = ("CREATE TABLE Race ( id smallint(6) unsigned NOT NULL AUTO_INCREMENT,  nom varchar(40) NOT NULL,  espece_id smallint(6) unsigned NOT NULL,  description text,  PRIMARY KEY (id)) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;")


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