import sqlite3
import pandas as pd

from pathlib import Path

from realtor_enums.RealtorEnums import RealtorEnums

DF_REQUEST = """SELECT DISTINCT latitude, longitude, fsa, round(avg(rent_price), 2) 
AS average_price FROM rent_prices GROUP BY fsa;"""


class DBConnector:
    def __init__(self):
        self.create_db_dirs()
        self.conn = sqlite3.connect(RealtorEnums.DB_PATH.value)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS rent_prices(
        latitude TEXT,
        longitude TEXT,
        postal_code TEXT,
        fsa TEXT,
        rent_price INTEGER)""")

    def save_distinct_to_db(self, data):
        for i in data:
            self.cur.execute("""INSERT OR IGNORE INTO rent_prices VALUES(?, ?, ?, ?, ?)""",
                             (i['latitude'], i['longitude'], i['postal_code'], i['fsa'], i['rent_price']))
            self.conn.commit()
            return i

    def get_data_frame(self):
        return pd.read_sql_query(DF_REQUEST, self.conn)

    def create_db_dirs(self):
        path = Path('rent-data-canada/database')
        if path.is_dir():
            pass
        else:path.mkdir(parents=True)

