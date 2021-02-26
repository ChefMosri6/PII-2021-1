from bottle import run, route

@route('/')
def index():
    return "welcome to bottle framework for Python on christian"


run(host='localhost', port=3000, debug= True)