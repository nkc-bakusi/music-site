import MySQLdb
import json

class DBAccess:

    sql_limit = 'LIMIT 1, 10'

    def __init__(self):
        self.connection = MySQLdb.connect(
            host='localhost',
            user='root',
            db='music_site',
            # passeord='',
            charset='utf8'
        )

    def get_music_list(self):
        cursor = self.connection.cursor()
        cursor.execute(
            'SELECT id, song_name, artist_name, play_time, CASE WHEN bpm BETWEEN 0 AND 50 THEN 1 WHEN bpm BETWEEN 50 AND 100 THEN 2 WHEN bpm > 100 THEN 3 END AS bpm_division FROM music ORDER BY RAND() LIMIT 10')
        itmes_list = []
        for row in cursor:
            itmes_list.append({
                'id': row[0],
                'song_name': row[1],
                'artist_name': row[2],
                'play_time': str(row[3]),
                'bpm_division': row[4]
            })
        return json.dumps({'data' : itmes_list})

    def get_music_list_playtime(self, playtime):
        cursor = self.connection.cursor()
        cursor.execute(
            'SELECT id, song_name, artist_name, play_time, CASE WHEN bpm BETWEEN 0 AND 50 THEN 1 WHEN bpm BETWEEN 50 AND 100 THEN 2 WHEN bpm > 100 THEN 3 END AS bpm_division FROM music ORDER BY RAND() LIMIT 10')
        itmes_list = []
        for row in cursor:
            itmes_list.append({
                'id': row[0],
                'song_name': row[1],
                'artist_name': row[2],
                'play_time': str(row[3]),
                'bpm_division': row[4]
            })
        return json.dumps({'data' : itmes_list})

    def get_music_list_bpm(self, bpm):
        sql = 'SELECT id, song_name, artist_name, play_time, CASE WHEN bpm BETWEEN 0 AND 50 THEN 1 WHEN bpm BETWEEN 50 AND 100 THEN 2 WHEN bpm > 100 THEN 3 END AS bpm_division, bpm FROM music '
        if (bpm == '1') :
            sql += 'WHERE bpm BETWEEN 0 and 49 '
        elif (bpm == '2') :
            sql += 'WHERE bpm BETWEEN 50 and 100 '
        else :
            sql += 'WHERE bpm > 100 '
        sql += 'ORDER BY RAND() LIMIT 10'
        cursor = self.connection.cursor()
        cursor.execute(sql)
        itmes_list = []
        for row in cursor:
            itmes_list.append({
                'id': row[0],
                'song_name': row[1],
                'artist_name': row[2],
                'play_time': str(row[3]),
                'bpm_division': row[4],
                'bpm' : row[5]
            })
        return json.dumps({'data' : itmes_list})

    def get_detail_music(self, music_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, song_name, artist_name, play_time, bpm FROM music WHERE id = %s', music_id)
        row = cursor.fetchone()
        itme_list = {
            'id': row[0],
            'song_name': row[1],
            'artist_name': row[2],
            'play_time': str(row[3]),
            'bpm': row[4]
        }
        return itme_list
