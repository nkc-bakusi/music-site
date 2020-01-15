from bottle import Bottle, route, run, template, get, static_file, error, request
from src.DBAccess import DBAccess
from distutils.util import strtobool
import pprint

# メイン画面
@route('/')
def index():
    return template('./views/index.html')

# 詳細画面
@route('/detail/<music_id>')
def detail(music_id):
    return template('./views/detail.html', music_data=DBAccess().get_detail_music(music_id))

# ここからWEBAPI
@route('/api/music', method='GET')
def db():
    is_first_access = request.query.get('search_condition')
    if (is_first_access == 'fast') :
        return DBAccess().get_music_list()
    elif (is_first_access == 'bpm') :
        return DBAccess().get_music_list_bpm(bpm)
    elif (is_first_access == 'play_time') :
        return DBAccess().get_music_list_playtime(playtime)
    else :
        return pprint.pformat(DBAccess().get_music_list())

# @route('/api/music/bpm', method='GET')
# def db():
#     return pprint.pformat(DBAccess().get_music_list())

# @route('/api/music/play_time', method='GET')
# def db():
#     return pprint.pformat(DBAccess().get_music_list())

# 各必要なstaticファイルパス
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@get("/static/img/<filepath:re:.*\.(jpg|png|svg|ico)>")
def img(filepath):
    return static_file(filepath, root="static/img")

# 404ステータスの場合
@error(404)
def error404(error):
    return '<h1>404 Page Not found'

run(host='localhost', port=8080, debug=True, reloader=True)
