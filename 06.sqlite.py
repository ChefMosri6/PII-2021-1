from bottle import route, run, template, static_file, request, get
import sqlite3
import sys


@route('/')
def index():
    # database connection
    connection = sqlite3.connect('./sqlite/univa.db')
    mycursor = connection.cursor()
    rows = mycursor.execute('SELECT * FROM students;')
    return template('index_new_copy.tpl', rows=rows, index="UNIVA.DB-SQlite" )
    mycursor.close()
    
run(host= 'localhost', port = 3000, debug = True, reloader = True)