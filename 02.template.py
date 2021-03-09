from bottle import run, route, template, view,static_file

@route('/')
def index():
    return template("welcome to {{ name}}, a python framewrok", name = "bottle version 0.12.19")

@route('/home')
@view('home_template')
def home():
    return dict(name = "bottle v0.12.19")

@route('/index')
@view('index_new')
def index():
    return dict(index = " Home")




@route('/contact')
@view('contact_new')
def contact():
    return dict(contact = "Contact information")

@route('/nvidia')
@view('nvidia_new')
def nvidia():
    return dict(nvidia = " Tarjetas de video Nvidia")

@route('/radeon')
@view('radeon_new')
def radeon():
    return dict(radeon = " Tarjetas de video Radeon")



run(host= "localhost", port=3000, debug=True, reloader=True)