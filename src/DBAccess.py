import MySQLdb

class DBAccess:
    sql_limit = "LIMIT 1, 10"

    def __init__(self) :
        self.connection = MySQLdb.connect(
            host='localhost',
            user='root',
            db='music_site',
            # passeord='',
            charset='utf8'
        )

    def get_music_list(self) :
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM music")
        itme_list = []
        for row in cursor:
            itme_list.append({
                "id": row[0],
                "song_name": row[1],
                "bpm": row[2],
                "artist_name": row[3],
                "play_time": row[4]
            })
        return itme_list

