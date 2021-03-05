from bottle import run, route, template, view

@route('/')
def index():
    return template("welcome to {{ name}}, a python framewrok", name = "bottle version 0.12.19")

@route('/home')
@view('home_template')
def home():
    return dict(name = "bottle v0.12.19")

run(host= "localhost", port=3000, debug=True, reloader=True)