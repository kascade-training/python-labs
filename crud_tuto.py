import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

cursor = db.cursor() 

crud=input("[c]reate, [r]ead, [u]pdate, [d]elete ")

#CREATE
if crud == "c":
    cru_cre=input("Creation [D]atabase, [T]able, (EXIT to go back) ")
    if cru_cre == "D":
        nom_db= input("nom ? ")
        cursor.execute("DROP DATABASE IF EXISTS {}".format(nom_db))
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(nom_db))
        cursor.execute("USE {}".format(nom_db))
    if cru_cre == "T":
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
    if cru_cre == "exit":

#READ
if crud == "r":
    nom_db=input("dans quelle database ? ")
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(nom_db))
    cursor.execute("USE {}".format(nom_db))
    crud_r=input("que lire ? [I]D, [T]able ")
    if crud_r =="I":
        nom_tb = input("Id de quelle table ?")
        cursor.execute("SELECT id from {}".format(nom_tb))
        list_id = cursor.fetchall()
        print(list_id)
    if crud_r== "T":
        nom_tb = input("nom de table ?")
        cursor.execute("SELECT * from {}".format(nom_tb))
        list_tb = cursor.fetchall()
        print(list_tb)
#UPDATE

#DELETE
if crud == "d":
    crud_del = input("delete [T]able, [D]atabase ? ")
    if crud_del == "D":
        nom_db=input("quelle database ? ")
        cursor.execute("DROP DATABASE {}".format(nom_db))
    if crud_del == "T":
        nom_tb=input("quelle table ? ")
<<<<<<< HEAD
        cursor.execute("DROP TABLE {}".format(nom_tb))
=======
        cursor.execute("DROP TABLE {}".format(nom_tb))
>>>>>>> d21f3800ca86c2cda70500902dcdaed703b126a4
