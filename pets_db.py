import mysql.connector as mysql

# Create Database
def create_database(nameDataBase):
    mysqldb = mysql.connect(host = "localhost", user = "root", password = "")
    mycursor = mysqldb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS {0}".format(nameDataBase))
    mycursor.execute("CREATE DATABASE {0}".format(nameDataBase))
    mycursor.execute("USE {0}".format(nameDataBase))
    mysqldb.close()
    
    return nameDataBase

# Create a table
def create_table(nameDataBase, nameTable):
    mysqldb = mysql.connect(host = "localhost", user = "root", password = "", database = "{0}".format(nameDataBase))   
    mycursor = mysqldb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS {0}(".format(nameTable))
    sql_stmt = "CREATE TABLE {0}".format(nameTable)
        
    if (nameTable == "Espece"):
        sql_stmt += "id smallint(6) unsigned NOT NULL AUTO_INCREMENT,\
                        nom_courant varchar(40) NOT NULL,\
                        nom_latin varchar(40) NOT NULL,\
                        description text,\
                        PRIMARY KEY (id),\
                        UNIQUE KEY nom_latin (nom_latin)"
    elif (nameTable == "Race"):
        sql_stmt += "id smallint(6) unsigned NOT NULL AUTO_INCREMENT,\
                        nom varchar(40) NOT NULL,\
                        espece_id smallint(6) unsigned NOT NULL,\
                        description text,\
                        PRIMARY KEY (id)"
    elif (nameTable == "Animal"):
        sql_stmt += "id smallint(6) unsigned NOT NULL AUTO_INCREMENT,\
                        sexe char(1) DEFAULT NULL,\
                        date_naissance datetime NOT NULL,\
                        nom varchar(30) DEFAULT NULL,\
                        commentaires text,\
                        espece_id smallint(6) unsigned NOT NULL,\
                        race_id smallint(6) unsigned DEFAULT NULL,\
                        mere_id smallint(6) unsigned DEFAULT NULL,\
                        pere_id smallint(6) unsigned DEFAULT NULL,\
                        PRIMARY KEY (id),\
                        UNIQUE KEY ind_uni_nom_espece_id (nom,espece_id)"

    sql_stmt += ") ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1"
    mysqldb.close()

    return nameTable 

# SELECT query
def read_to_table(nameTable, query, connection):
    sql_stmt = "SELECT * FROM {0} {1}".format(nameTable, query)
    cursor = connection.cursor()
    cursor.execute(sql_stmt)
    records = cursor.fetchall()
    print(records)
    cursor.close()

# INSERT query
def insert_to_table(nameTable, connection):
    deco = input("Enter the \{\"FIELDS\":\"VALUES\"\} :")
    sql_stmt = "INSERT INTO {0} {1} VALUES {2}".format(nameTable, ",".join(list(deco.keys())), ",".join(list(deco.values())))
    cursor = connection.cursor()
    cursor.execute(sql_stmt)
    connection.commit()
    cursor.close()

# UPDATE query
def update_to_table(nameTable, id, connection):
    deco = input("Enter the \{\"FIELDS:\"VALUES\"\} :")
    sql_stmt = "UPDATE {0} SET ".format(nameTable, ",".join(list(deco.keys())), ",".join(list(deco.values())))
    cursor = connection.cursor()
    cursor.execute(sql_stmt, id)
    connection.commit()
    cursor.close()

# DELETE query
def delete_to_table(nameTable, id, connection):
    sql_stmt = "DELETE FROM {0} WHERE id = {1}".format(nameTable, id)
    cursor = connection.cursor()
    cursor.execute(sql_stmt)
    connection.commit()
    cursor.close()

# DELETE query
def rud_to_table(nameDataBase, nameTable, choice):

    connection = mysql.connect(host = "localhost", user = "root", password = "", database = "{0}".format(nameDataBase))

    if choice == "2":
        query = input("Enter the query : ") 
        read_to_table(nameTable, query, connection)
    elif choice == "3":
        insert_to_table(nameTable, connection)
    elif choice == "4":
        id = input("Enter the ID : ") 
        update_to_table(nameTable, id, connection)
    elif choice == "5":
        id = input("Enter the ID : ") 
        delete_to_table(nameTable, id, connection)

    connection.close()

title = "PETS DB - Create, Read, Insert, Update, Delete"

print('Select the action that you need to perform')
print('1.Create DataBase or Table')
print('2.Read to Table')
print('3.Insert to Table')
print('4.Update to Table')
print('5.Delete to Table\n')

choice = input("Enter your selection number: ")
nameDataBase = ""
nameTable = ""

if (choice == "1"):
    print('1.Create DataBase')
    print('2.Create Table')
    name = input("Enter the name: ")
    
    if (int(name.split(".")[0]) == 1):
        nameDataBase = create_database(str(name.split(".")[1]))
    elif (nameDataBase != "" and int(name.split(".")[0]) == 2):
        if (nameDataBase == ""):
            nameDataBase = create_database(str(name.split(".")[1]))    
        nameTable = create_table(nameDataBase, str(name.split(".")[1]))
    
elif (nameTable != "" and (choice == "2" or choice == "3" or choice == "4" or choice == "5")):   
    rud_to_table(nameDataBase, nameTable, choice)

else:
    print("Invalid Selection. Please select a number that is between 1 and 5")