from bottle import run, route, template, view

@route('/')
def home():
    return "welcome to bottle framework for Python on christian"



run(host='localhost', port=3000, debug= True, reloader=True)
