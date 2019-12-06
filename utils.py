from flask import make_response
import pymysql.cursors  

JSON_MIME_TYPE = 'application/json'


def search_book(books, book_id):
    for book in books:
        if book['id'] == book_id:
            return book


def connectAnimal():
    connection = pymysql.connect(host='localhost', user='root', password='', db='m2i_python_db')
    
    print ("connect successful!!")

    try:
        with connection.cursor() as cursor:  
            sql = "SELECT * FROM Animal"
            cursor.execute(sql)         
            res = cursor.fetchall()
    finally:
        connection.close()
    return str(res)

def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)
