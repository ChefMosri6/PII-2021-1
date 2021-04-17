from bottle import route, run, template, static_file, request, get, post
import sqlite3
import sys

@route('/')
def index():
    return "testing server SQlite running for INSERT"

@route('/insert')
def inSERT():
    # database connection
    connection = sqlite3.connect('./sqlite/univa.db')
    mycursor = connection.cursor()
    rows = mycursor.execute('SELECT * FROM students;')
    return template('index.tpl', rows=rows, name="UNIVA.DB-SQlite" )
    mycursor.close()
    
run(host= 'localhost', port = 3000, debug = True, reloader = True)