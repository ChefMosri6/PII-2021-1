from bottle import run, route, template, view

@route('/')
def index():
    return name("welcome to {{ name}}, a python framewrok", name = "bottle version 0.12.19")



run(host= "localhost", port=3000, debug=True, reloader=True)