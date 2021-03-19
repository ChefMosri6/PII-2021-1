from bottle import run, route, template, view,static_file

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, route = './static/')
@route('/')
def index():
    return name("welcome to {{ name}}, a python framewrok", name = "bottle version 0.12.19")

@route('/home')
@view('home_template')
def home():
    return dict(name = "bottle v0.12.19")

@route('/contact')
@view('contact_new')
def contact():
    return dict(name = "Contact information")

@route('/nvidia')
@view('nvidia_new')
def nvidia():
    return dict(name = " Tarjetas de video Nvidia")

@route('/radeon')
@view('radeon_new')
def radeon():
    return dict(name = " Tarjetas de video Radeon")

run(host= "localhost", port=3000, debug=True, reloader=True)