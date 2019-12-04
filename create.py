import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursor = db.cursor() 

new= (input("Creation [D]atabase, [T]able, (EXIT to go back) "))
if new == "D":
    nom_db= input("nom ? ")
    cursor.execute("DROP DATABASE IF EXISTS {}".format(nom_db))
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(nom_db))
    cursor.execute("USE {}".format(nom_db))
if new == "T":
    nom_db=input("dans quelle database ? ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(nom_db))
    cursor.execute("USE {}".format(nom_db))
    nom_tb=input("nom de la table ? ESPECE, RACE, ANIMAL ")
    if nom_tb == "ESPECE":
        cursor.execute("""CREATE TABLE IF NOT EXISTS Animal (
                    id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
                    sexe char(1) DEFAULT NULL,
                    date_naissance datetime NOT NULL,
                    nom varchar(30) DEFAULT NULL,
                    commentaires text,
                    espece_id smallint(6) unsigned NOT NULL,
                    race_id smallint(6) unsigned DEFAULT NULL,
                    mere_id smallint(6) unsigned DEFAULT NULL,
                    pere_id smallint(6) unsigned DEFAULT NULL,
                    PRIMARY KEY (id),
                    UNIQUE KEY ind_uni_nom_espece_id (nom,espece_id)
                    ) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;""")
    elif nom_tb == "RACE":
        cursor.execute("""CREATE TABLE IF NOT EXISTS Race (
                id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
                nom varchar(40) NOT NULL,
                espece_id smallint(6) unsigned NOT NULL,
                description text,
                PRIMARY KEY (id)) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;""")
    elif nom_tb == "ANIMAL":
        cursor.execute("""CREATE TABLE Animal (
                id smallint(6) unsigned NOT NULL AUTO_INCREMENT,
                sexe char(1) DEFAULT NULL,
                date_naissance datetime NOT NULL,
                nom varchar(30) DEFAULT NULL,
                commentaires text,
                espece_id smallint(6) unsigned NOT NULL,
                race_id smallint(6) unsigned DEFAULT NULL,
                mere_id smallint(6) unsigned DEFAULT NULL,
                pere_id smallint(6) unsigned DEFAULT NULL,
                PRIMARY KEY (id),
                UNIQUE KEY ind_uni_nom_espece_id (nom,espece_id)
                ) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;""")
    else:
        print("fonction pas encore implémentée, attendez 2 semaines")
if new == "exit":
    break    

