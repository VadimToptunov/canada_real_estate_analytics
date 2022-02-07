import pandas as pd


class DataCleaner:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.clean_data()

    def clean_data(self):
        # ToDo: Get Unique data by latitude and longitude
        df = pd.read_csv(self.csv_file)
        grouped_df = df.groupby('fsa')['rent_price'].mean()
        grouped_df.reset_index()
        return grouped_df
