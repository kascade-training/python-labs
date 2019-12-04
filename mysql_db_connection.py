## importing 'mysql.connector' as mysql for convenient
## pip install mysql-connector-python

import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)
print(db) # it will print a connection object if everything is fine

def main (): 
    db1 = input ("créer une base de donnée if not exist (oui/non)") 
    if db1 == "Non":
        print("database non créér")
    if db1 == "oui":
        nomdb=input("entrez le nom de la databases")
        cursor = db.cursor()
       # cursor.execute("CREATE DATABASE IF NOT EXISTS %s", (nomdb,))
        cursor.execute("CREATE DATABASE IF NOT EXISTS " +nomdb)
        cursor.execute("USE " +nomdb)
        cursor.execute("CREATE TABLE IF NOT EXISTS Animal (id smallint(6) unsigned NOT NULL AUTO_INCREMENT, sexe char(1) DEFAULT NULL, date_naissance datetime NOT NULL, nom varchar(30) DEFAULT NULL, commentaires text, espece_id smallint(6) unsigned NOT NULL, race_id smallint(6) unsigned DEFAULT NULL, mere_id smallint(6) unsigned DEFAULT NULL, pere_id smallint(6) unsigned DEFAULT NULL, PRIMARY KEY (id), UNIQUE KEY ind_uni_nom_espece_id (nom,espece_id)) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8")
        cursor.execute("CREATE TABLE IF NOT EXISTS Espece (id smallint(6) unsigned NOT NULL AUTO_INCREMENT, nom_courant varchar(40) NOT NULL, nom_latin varchar(40) NOT NULL, description text, PRIMARY KEY (id), UNIQUE KEY nom_latin (nom_latin)) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1")
        cursor.execute("CREATE TABLE Race IF NOT EXISTS (id smallint(6) unsigned NOT NULL AUTO_INCREMENT, nom varchar(40) NOT NULL, espece_id smallint(6) unsigned NOT NULL, description text, PRIMARY KEY (id)) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1")
if __name__ == '__main__': 
    main() 