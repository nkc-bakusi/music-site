from bottle import route, run, template, error

@route('/')
def index():
    return template('Hello {{ title }} page!!', title='top')

@error(404)
def error404(error):
    return '<h1>404 Page Not found'


run(host='localhost', port=8080, debug=True, reloader=True)
