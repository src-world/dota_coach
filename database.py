import sqlite3

def init_db():
    conn = sqlite3.connect("dota_bot.db")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS tilt_diary (
                user_id INTEGER
                match_id INTEGER
                result TEXT
                tilt_level INTEGER
                hero TEXT
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
""")
    conn.commit()
    conn.close