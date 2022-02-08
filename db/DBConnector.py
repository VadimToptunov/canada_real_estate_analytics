import sqlite3
import pandas as pd

DATABASE = "./database/apptdata.db"
DF_REQUEST = """SELECT DISTINCT fsa, ROUND(AVG(rent_price), 2) as average_price 
            FROM appt_rent_prices GROUP BY fsa;"""


class DBConnector:
    def __init__(self,):
        self.conn = sqlite3.connect(DATABASE)

    def add_data_to_db(self, data):
        df = pd.DataFrame(data)
        df.to_sql('appt_rent_prices', self.conn, if_exists='append', index=False)

    def get_data_frame(self):
        return pd.read_sql_query(DF_REQUEST, self.conn)
