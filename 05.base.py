from bottle import run, route, template, view, static_file 

@route('/')
def home():
    return "welcome to bottle framework for Python on christian"

@route('/index')
@view('index_new copy')
def index():
    return dict(name = " index")
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, route = './static/')

run(host='localhost', port=3000, debug= True, reloader= True)