import sqlite3

from flask_sqlalchemy.model import Model
from sqlalchemy.testing import db

from . import models

from flask_sqlalchemy import SQLAlchemy


# TABLENAME = "rent_prices"


class Flats():
    query = None
    db = None
    homeid = ""
    latlong = ""
    latitude = ""
    longitude = ""
    postal_code = ""
    fsa = ""
    rent_price = 0

    def __init__(self, flask_sqlalchemy):
        self.db = SQLAlchemy(flask_sqlalchemy)
        self.setDB()

    def setDB(self):
        self.homeid = self.db.Column(self.db.String, primary_key=True)
        self.latlong = self.db.Column(self.db.String, unique=True)
        self.latitude = self.db.Column(self.db.String)
        self.longitude = self.db.Column(self.db.String)
        self.postal_code = self.db.Column(self.db.String)
        self.fsa = self.db.Column(self.db.String)
        self.rent_price = self.db.Column(self.db.Integer)

    def __repr__(self):
        return f'<Flat {self.homeid} {self.postal_code}>'

# def connect():
#     conn = sqlite3.connect(DB_PATH)
#     cur = conn.cursor()
#     cur.execute(f"""CREATE TABLE IF NOT EXISTS {TABLENAME}(
#         latitude TEXT,
#         longitude TEXT,
#         postal_code TEXT,
#         fsa TEXT,
#         rent_price INTEGER)""")
#     conn.commit()
#     conn.close()


# def view():
#     conn = sqlite3.connect(DB_PATH)
#     cur = conn.cursor()
#     cur.execute(
#         f"""SELECT latitude, longitude, fsa, round(avg(rent_price), 2) AS average_price FROM {TABLENAME} group by fsa;""")
#     rows = cur.fetchall()
#     flats = []
#     for i in rows:
#         flat = models.Flats(i[0], i[1], i[2], i[3])
#         flats.append(flat)
#     conn.close()
#     return flats
