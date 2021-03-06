import MySQLdb
import json


class DBAccess:

    template_sql = 'SELECT id, song_name, artist_name, bpm, play_time,'\
            'CASE WHEN bpm BETWEEN 0 AND 50 THEN 1 WHEN bpm '\
            'BETWEEN 50 AND 100 THEN 2 WHEN bpm > 100 THEN 3 END AS bpm_division, '\
            'CASE WHEN play_time BETWEEN \'00:00:00\' AND \'02:59:00\' THEN 1 WHEN play_time '\
            'BETWEEN \'03:00:00\' AND \'03:59:00\' THEN 2 WHEN play_time > \'04:00:00\' THEN 3 END AS play_time_division '\
            'FROM music '

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
            self.template_sql + 
            'ORDER BY RAND() LIMIT 10'
        )
        itmes_list = []
        for row in cursor:
            itmes_list.append({
                'id': row[0],
                'song_name': row[1],
                'artist_name': row[2],
                'play_time': str(row[3]),
                'bpm_division': row[4],
                'play_time_division': row[5]
            })
        return json.dumps({'data': itmes_list})

    def get_music_list_playtime(self, playtime):
        sql = self.template_sql
        if (playtime == '1'):
            sql += 'WHERE play_time BETWEEN \'00:00:00\' AND \'02:59:00\' '
        elif (playtime == '2'):
            sql += 'WHERE play_time BETWEEN \'03:00:00\' AND \'03:59:00\' '
        else:
            sql += 'WHERE play_time > \'04:00:00\' '
        cursor = self.connection.cursor()
        cursor.execute(sql)
        itmes_list = []
        for row in cursor:
            itmes_list.append({
                'id': row[0],
                'song_name': row[1],
                'artist_name': row[2],
                'bpm': row[3],
                'play_time': str(row[4]),
                'bpm_division': row[5],
                'play_time_division': row[6]
            })
        return json.dumps({'data': itmes_list})

    def get_music_list_bpm(self, bpm):
        sql = self.template_sql
        if (bpm == '1'):
            sql += 'WHERE bpm BETWEEN 0 and 49 '
        elif (bpm == '2'):
            sql += 'WHERE bpm BETWEEN 50 and 100 '
        else:
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
                'bpm': row[3],
                'play_time': str(row[4]),
                'bpm_division': row[5],
                'play_time_division': row[6]
            })
        return json.dumps({'data': itmes_list})

    def get_detail_music(self, music_id):
        cursor = self.connection.cursor()
        sql = 'SELECT id, song_name, artist_name, play_time, bpm, mp3data FROM music WHERE id=\'%s\'' % music_id
        cursor.execute(sql)
        row = cursor.fetchone()
        itme_list = {
            'id': row[0],
            'song_name': row[1],
            'artist_name': row[2],
            'play_time': str(row[3]),
            'bpm': row[4],
            'mp3data': row[5]
        }
        return itme_list
