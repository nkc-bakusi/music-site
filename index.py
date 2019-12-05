from bottle import route, run, template, get, static_file, error

@route('/')
def index():
    return template('./views/index.html')

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@get("/static/img/<filepath:re:.*\.(jpg|png|svg|ico)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@error(404)
def error404(error):
    return '<h1>404 Page Not found'

run(host='localhost', port=8080, debug=True, reloader=True)
