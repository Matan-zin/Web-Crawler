import sqlite3


con = sqlite3.connect('webcrawler.db')

cur = con.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS tbl_pastes
(
    id integer UNIQUE NOT NULL,
    title VARCHAR,
    author VARCHAR,
    date TIMESTAMP,
    content VARCHAR
);
''')


con.commit()

for row in cur.execute("select * from tbl_pastes"):
    print(row)