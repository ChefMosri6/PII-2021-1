from bottle import run, route,error, abort 
@error(400)
def bad_request(error):
    return "400 bad request"

@route('/')
def index():
    return "Welcome to bootle Python Web Framework"

@route('/bad_request_route')
def bad_request_route():
    abort(400)
    
@error(401)
def unauthorized(error):
    return "401 unautorized"

@route('/unautorized')
def unauthorized():
    abort(401)


run(host='localhost', port=3002, debug=True,relader =True)

