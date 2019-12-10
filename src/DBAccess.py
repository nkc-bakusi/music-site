import MySQLdb

class DBAccess:
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
                "name": row[1]
            })
        return itme_list

