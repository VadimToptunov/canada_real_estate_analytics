import sqlite3
import pandas as pd

from pathlib import Path

from gathering_scripts.realtor_enums.RealtorEnums import RealtorEnums

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
        homeid TEXT PRIMARY KEY,
        latlong TEXT UNIQUE,
        latitude TEXT,
        longitude TEXT,
        postal_code TEXT,
        fsa TEXT,
        rent_price INTEGER)""")

    def save_distinct_to_db(self, data):
        cursor = self.cur
        connection = self.conn
        for i in data:
            homeid = i["_id"]
            latlong = i["latlong"]
            lat = i['latitude']
            longt = i['longitude']
            code = i['postal_code']
            fsa = i['fsa']
            price = i['rent_price']
            cursor.execute("INSERT OR REPLACE INTO rent_prices(homeid, latlong, latitude, longitude, postal_code, fsa, "
                           "rent_price) VALUES(?,?,?,?,?,?,?)", (homeid, latlong, lat, longt, code, fsa, price))

            connection.commit()

    def get_data_frame(self):
        return pd.read_sql_query(DF_REQUEST, self.conn)

    def create_db_dirs(self):
        path = Path('rent-data-canada/database')
        if path.is_dir():
            pass
        else:
            path.mkdir(parents=True)
