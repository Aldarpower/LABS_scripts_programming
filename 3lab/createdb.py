import sqlite3

connecttoDB = sqlite3.connect('posts.db')
db = connecttoDB.cursor()
db.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT,
        body TEXT
    )
''')
connecttoDB.commit()
connecttoDB.close()