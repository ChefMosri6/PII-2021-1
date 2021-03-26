from bottle import route, run, template, static_file, request, get,
import sqlite3
import sys


@route('/')
def index():
    # database connection
    connection = sqlite3.connect('./sqlite-tools-win32-x86-3350200/univa.db')
    mycursor = connection.cursor()
    raws = mycursor.execute('SELECT * FROM students;')
    return template('index.tpl', raws=raws)
    mycursor.close()