import json
from flask import Flask, Response, abort
from .utils import JSON_MIME_TYPE
import pymysql

app = Flask(__name__)

db = pymysql.connect("localhost", "root", "", "pandi" )

@app.route('/animals')
def animal_list():
    cursor = db.cursor()
    sql = "SELECT nom FROM animal"
    cursor.execute(sql)
    results = cursor.fetchall()
    response = Response(
        json.dumps(results), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.errorhandler(404)
def not_found(e):
    return '', 404
