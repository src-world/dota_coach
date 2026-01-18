import sqlite3

conn = sqlite3.connect("dota_bot.db")
cur = conn.cursor()

def init_db():
    cur.execute("""
            CREATE TABLE IF NOT EXISTS tilt_diary (
            user_id INTEGER,
            date TEXT,
            result TEXT,
            anger_level INTEGER
    )
""")
    conn.commit()
    conn.close

