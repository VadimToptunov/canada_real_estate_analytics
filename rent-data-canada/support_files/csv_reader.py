import pandas as pd

def get_data(city: str):
    df = pd.read_csv(f'{city.lower()}_data_2021-10-06.csv', sep=';')
    print(df)
    print(f"Averge price for 1 bedroom apartment in {city}: {int(df['Price'].mean())}")

if __name__ == '__main__':
    get_data("Montreal")