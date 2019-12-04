# -*- coding: utf-8 -*-

## pip install mysql-connector-python

import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

# CRUD Create Read Update Delete

input_choice='0'
while input_choice != 'exit':
    input_choice = input('Choix d action sur la base de donnée: \n * Pour créer la base de donnée pets_db appuyer sur 1. \n * Pour lire la base de donnée pets_db appuyer sur 2. \n * Pour mettre a jour la base de donnée appuyer sur 3. \n * Pour effacer la base de donnée appuyer sur 4. \n * Pour sortir de l application taper exit.')
    if input_choice == '1' :
        
        # CRUD Create
        ## creating a databse called 'pets_db'
        ## 'execute()' method is used to compile a 'SQL' statement
        ## below statement is used to create tha database
        cursor.execute("DROP DATABASE IF EXISTS pets_db")
        cursor.execute("CREATE DATABASE IF NOT EXISTS pets_db")
        cursor.execute("USE pets_db")
        ## below statement is used to create TABLES
        cursor.execute("SET NAMES utf8")
        cursor.execute("CREATE TABLE  Espece (id smallint(6) unsigned NOT NULL AUTO_INCREMENT,nom_courant varchar(40) NOT NULL,nom_latin varchar(40) NOT NULL,description text,PRIMARY KEY (id),UNIQUE KEY nom_latin (nom_latin)) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1")
        cursor.execute("CREATE TABLE  Race (id smallint(6) unsigned NOT NULL AUTO_INCREMENT,nom varchar(40) NOT NULL,espece_id smallint(6) unsigned NOT NULL,description text,PRIMARY KEY (id)) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1")
        cursor.execute("CREATE TABLE  Animal (id smallint(6) unsigned NOT NULL AUTO_INCREMENT,sexe char(1) DEFAULT NULL,date_naissance datetime NOT NULL,nom varchar(30) DEFAULT NULL,commentaires text,espece_id smallint(6) unsigned NOT NULL,race_id smallint(6) unsigned DEFAULT NULL,mere_id smallint(6) unsigned DEFAULT NULL,pere_id smallint(6) unsigned DEFAULT NULL,PRIMARY KEY (id),UNIQUE KEY ind_uni_nom_espece_id (nom,espece_id)) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8")


    # CRUD Read

    ## executing the statement using 'execute()' method
    ## affiche le contenu des tables
    if input_choice == '2' :
        cursor.execute("USE pets_db")
        cursor.execute("SHOW TABLES")
        ## 'fetchall()' method fetches all the rows from the last executed statement
        tables = cursor.fetchall() ## it returns a list of all tables present

        ## printing the list of tables
        print(tables)

        ## showing one by one tables
        for table in tables:
            print(table)

        cursor.execute("SELECT * FROM pets_db.animal")
        ## 'fetchall()' method fetches all the rows from the last executed statement
        animals = cursor.fetchall() ## it returns a list of all animals present

        ## showing one by one animal
        for animal in animals:
            print(animal)
             
        cursor.execute("SELECT * FROM pets_db.race")
        ## 'fetchall()' method fetches all the rows from the last executed statement
        races = cursor.fetchall() ## it returns a list of all animals present

        ## showing one by one animal
        for race in races:
            print(race)


        cursor.execute("SELECT * FROM pets_db.espece")
                ## 'fetchall()' method fetches all the rows from the last executed statement
        especes = cursor.fetchall() ## it returns a list of all animals present

        ## showing one by one animal
        for espece in especes:
            print(espece)


    
    # CRUD Update
    ## Enrichie les tables de pets_db

    if input_choice == '3' :
        cursor.execute("USE pets_db")
        cursor.execute("INSERT INTO pets_db.espece VALUES (1,'Chien','Canis canis','Bestiole à quatre pattes qui aime les caresses et tire souvent la langue'),(2,'Chat','Felis silvestris','Bestiole à quatre pattes qui saute très haut et grimpe aux arbres'),(3,'Tortue d''Hermann','Testudo hermanni','Bestiole avec une carapace très dure'),(4,'Perroquet amazone','Alipiopsitta xanthops','Joli oiseau parleur vert et jaune')")
        cursor.execute("INSERT INTO pets_db.race VALUES (1,'Berger allemand',1,'Chien sportif et élégant au pelage dense, noir-marron-fauve, noir ou gris.'),(2,'Berger blanc suisse',1,'Petit chien au corps compact, avec des pattes courtes mais bien proportionnées et au pelage tricolore ou bicolore.'),(3,'Singapura',2,'Chat de petite taille aux grands yeux en amandes.'),(4,'Bleu russe',2,'Chat aux yeux verts et à la robe épaisse et argentée.'),(5,'Maine coon',2,'Chat de grande taille, à poils mi-longs.'),(7,'Sphynx',2,'Chat sans poils.'),(8,'Nebelung',2,'Chat bleu russe, mais avec des poils longs...')")
        cursor.execute("INSERT INTO pets_db.animal VALUES (1,'M','2010-04-05 13:43:00','Rox','Mordille beaucoup',1,1,18,22),(2,NULL,'2010-03-24 02:23:00','Roucky',NULL,2,NULL,40,30),(3,'F','2010-09-13 15:02:00','Schtroumpfette',NULL,2,4,41,31),(4,'F','2009-08-03 05:12:00',NULL,'Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(5,NULL,'2010-10-03 16:44:00','Choupi','Né sans oreille gauche',2,NULL,NULL,NULL),(6,'F','2009-06-13 08:17:00','Bobosse','Carapace bizarre',3,NULL,NULL,NULL),(7,'F','2008-12-06 05:18:00','Caroline',NULL,1,2,NULL,NULL),(8,'M','2008-09-11 15:38:00','Bagherra',NULL,2,5,NULL,NULL),(9,NULL,'2010-08-23 05:18:00',NULL,'Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(10,'M','2010-07-21 15:41:00','Bobo',NULL,1,NULL,7,21),(11,'F','2008-02-20 15:45:00','Canaille',NULL,1,NULL,NULL,NULL),(12,'F','2009-05-26 08:54:00','Cali',NULL,1,2,NULL,NULL),(13,'F','2007-04-24 12:54:00','Rouquine',NULL,1,1,NULL,NULL),(14,'F','2009-05-26 08:56:00','Fila',NULL,1,2,NULL,NULL),(15,'F','2008-02-20 15:47:00','Anya',NULL,1,NULL,NULL,NULL),(16,'F','2009-05-26 08:50:00','Louya',NULL,1,NULL,NULL,NULL),(17,'F','2008-03-10 13:45:00','Welva',NULL,1,NULL,NULL,NULL),(18,'F','2007-04-24 12:59:00','Zira',NULL,1,1,NULL,NULL),(19,'F','2009-05-26 09:02:00','Java',NULL,1,2,NULL,NULL),(20,'M','2007-04-24 12:45:00','Balou',NULL,1,1,NULL,NULL),(21,'F','2008-03-10 13:43:00','Pataude',NULL,1,NULL,NULL,NULL),(22,'M','2007-04-24 12:42:00','Bouli',NULL,1,1,NULL,NULL),(24,'M','2007-04-12 05:23:00','Cartouche',NULL,1,NULL,NULL,NULL),(25,'M','2006-05-14 15:50:00','Zambo',NULL,1,1,NULL,NULL),(26,'M','2006-05-14 15:48:00','Samba',NULL,1,1,NULL,NULL),(27,'M','2008-03-10 13:40:00','Moka',NULL,1,NULL,NULL,NULL),(28,'M','2006-05-14 15:40:00','Pilou',NULL,1,1,NULL,NULL),(29,'M','2009-05-14 06:30:00','Fiero',NULL,2,3,NULL,NULL),(30,'M','2007-03-12 12:05:00','Zonko',NULL,2,5,NULL,NULL),(31,'M','2008-02-20 15:45:00','Filou',NULL,2,4,NULL,NULL),(32,'M','2009-07-26 11:52:00','Spoutnik',NULL,3,NULL,52,NULL),(33,'M','2006-05-19 16:17:00','Caribou',NULL,2,4,NULL,NULL),(34,'M','2008-04-20 03:22:00','Capou',NULL,2,5,NULL,NULL),(35,'M','2006-05-19 16:56:00','Raccou','Pas de queue depuis la naissance',2,4,NULL,NULL),(36,'M','2009-05-14 06:42:00','Boucan',NULL,2,3,NULL,NULL),(37,'F','2006-05-19 16:06:00','Callune',NULL,2,8,NULL,NULL),(38,'F','2009-05-14 06:45:00','Boule',NULL,2,3,NULL,NULL),(39,'F','2008-04-20 03:26:00','Zara',NULL,2,5,NULL,NULL),(40,'F','2007-03-12 12:00:00','Milla',NULL,2,5,NULL,NULL),(41,'F','2006-05-19 15:59:00','Feta',NULL,2,4,NULL,NULL),(42,'F','2008-04-20 03:20:00','Bilba','Sourde de l''oreille droite à 80%',2,5,NULL,NULL),(43,'F','2007-03-12 11:54:00','Cracotte',NULL,2,5,NULL,NULL),(44,'F','2006-05-19 16:16:00','Cawette',NULL,2,8,NULL,NULL),(45,'F','2007-04-01 18:17:00','Nikki','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(46,'F','2009-03-24 08:23:00','Tortilla','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(47,'F','2009-03-26 01:24:00','Scroupy','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(48,'F','2006-03-15 14:56:00','Lulla','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(49,'F','2008-03-15 12:02:00','Dana','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(50,'F','2009-05-25 19:57:00','Cheli','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(51,'F','2007-04-01 03:54:00','Chicaca','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(52,'F','2006-03-15 14:26:00','Redbul','Insomniaque',3,NULL,NULL,NULL),(54,'M','2008-03-16 08:20:00','Bubulle','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(55,'M','2008-03-15 18:45:00','Relou','Surpoids',3,NULL,NULL,NULL),(56,'M','2009-05-25 18:54:00','Bulbizard','Bestiole avec une carapace très dure',3,NULL,NULL,NULL),(57,'M','2007-03-04 19:36:00','Safran','Coco veut un gâteau !',4,NULL,NULL,NULL),(58,'M','2008-02-20 02:50:00','Gingko','Coco veut un gâteau !',4,NULL,NULL,NULL),(59,'M','2009-03-26 08:28:00','Bavard','Coco veut un gâteau !',4,NULL,NULL,NULL),(60,'F','2009-03-26 07:55:00','Parlotte','Coco veut un gâteau !',4,NULL,NULL,NULL),(61,'M','2010-11-09 00:00:00','Yoda',NULL,2,5,NULL,NULL)")
        
        cursor.execute("ALTER TABLE race ADD CONSTRAINT fk_race_espece_id FOREIGN KEY (espece_id) REFERENCES Espece (id) ON DELETE CASCADE")
        cursor.execute("ALTER TABLE Animal ADD CONSTRAINT fk_pere_id FOREIGN KEY (pere_id) REFERENCES Animal (id) ON DELETE SET NULL")
        cursor.execute("ALTER TABLE Animal ADD CONSTRAINT fk_espece_id FOREIGN KEY (espece_id) REFERENCES Espece (id)")
        cursor.execute("ALTER TABLE Animal ADD CONSTRAINT fk_mere_id FOREIGN KEY (mere_id) REFERENCES Animal (id) ON DELETE SET NULL")
        cursor.execute("ALTER TABLE Animal ADD CONSTRAINT fk_race_id FOREIGN KEY (race_id) REFERENCES Race (id) ON DELETE SET NULL")
        
        db.commit()
    

    # CRUD Delete
    if input_choice == '4' :
        cursor.execute("DROP DATABASE IF EXISTS pets_db")
        print("La base pets à été supprimée.")

    # # Pour sortir de l'application
    if input_choice == 'exit' :
        break

