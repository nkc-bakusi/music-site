from bottle import Bottle, route, run, template, get, static_file, error
from src.DBAccess import DBAccess
import pprint

app = Bottle()

@app.route('/')
def index():
    return template('./views/index.html')

@app.route('/detail')
def index():
    return template('./views/index.html')

@app.route('/api/music', method='GET')
def db():
    return pprint.pformat(DBAccess().get_music_list())

@app.route('/api/music/bpm', method='GET')
def db():
    return pprint.pformat(DBAccess().get_music_list())

@app.route('/api/music/play_time', method='GET')
def db():
    return pprint.pformat(DBAccess().get_music_list())

@app.get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@app.get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@app.get("/static/img/<filepath:re:.*\.(jpg|png|svg|ico)>")
def img(filepath):
    return static_file(filepath, root="static/img")

@app.error(404)
def error404(error):
    return '<h1>404 Page Not found'

run(host='localhost', port=8080, debug=True, reloader=True)
