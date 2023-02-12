import sqlite3


con = sqlite3.connect('/Crawler/database/webcrawler.db')

cur = con.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS tbl_pastes
(
    id integer UNIQUE NOT NULL,
    title VARCHAR,
    author VARCHAR,
    date TIMESTAMP,
    content VARCHAR
)
''')


con.commit()