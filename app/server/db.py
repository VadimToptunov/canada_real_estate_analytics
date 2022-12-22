import sqlite3
from . import models

TABLENAME = "rent_prices"
DB_PATH = "../gathering_scripts/rent-data-canada/database/apptdata.db"


def connect():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {TABLENAME}(
        latitude TEXT,
        longitude TEXT,
        postal_code TEXT,
        fsa TEXT,
        rent_price INTEGER)""")
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(f"""SELECT DISTINCT latitude, longitude, fsa, round(avg(rent_price), 2) 
AS average_price FROM {TABLENAME} GROUP BY fsa;""")
    rows = cur.fetchall()
    flats = []
    for i in rows:
        flat = models.Flats(i[0], i[1], i[2], i[3])
        flats.append(flat)
    conn.close()
    return flats
