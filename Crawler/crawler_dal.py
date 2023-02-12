import sqlite3

from model.paste import Paste

DB_PATH = '/Crawler/database/webcrawler.db'

class CrawlerDal:



    def save_paste(self, paste: Paste):

        try:

            con = sqlite3.connect(DB_PATH)

            cur = con.cursor()

            cur.execute("INSERT INTO tbl_pastes VALUES(?,?,?,?,?)",
            [
                paste.get_hash(), 
                paste.get_title(), 
                paste.get_author(), 
                paste.get_date(), 
                paste.get_content()
            ])

            con.commit()
        
        except Exception as e:
            print(e)
