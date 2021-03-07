from bottle import run,route, redirect

@route('/') 
def index():
    return "Running bottle with python on Univa"

@route('/restriected')
def restriected():
    print("using restriected method")
    redirect('/')

run(host='localhost', port=3001, debug =True, reloader=True)
