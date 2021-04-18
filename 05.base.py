from bottle import run, route, template, view, static_file

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root ='./static/')

@route('/')
def home():
    return "welcome to bottle framework for Python on christian"

@route('/index_new_copy')
@view('index_new_copy')
def index_new_copy():
    return dict(index = "index")

@route('/contact_new')
@view('contact_new')
def contact_new():
    return dict(contact  = "Ubicacion y contactos")

@route('/nvidia_new')
@view('nvidia_new')
def nvidia_new():
    return dict(nvidia  = "nvidia")

@route('/radeon_new')
@view('radeon_new')
def radeon_new():
    return dict(radeon  = "radeon")


    

run(host='localhost', port=3000, debug= True, reloader=True)