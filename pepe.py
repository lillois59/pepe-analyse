#!/usr/bin/env python
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def banner():
    font = """


                                                 _
 _ __    ___  _ __    ___    __ _  _ __    __ _ | | _   _  ___   ___  _ __
| '_ \  / _ \| '_ \  / _ \  / _` || '_ \  / _` || || | | |/ __| / _ \| '__|
| |_) ||  __/| |_) ||  __/ | (_| || | | || (_| || || |_| |\__ \|  __/| |
| .__/  \___|| .__/  \___|  \__,_||_| |_| \__,_||_| \__, ||___/ \___||_|
|_|          |_|                                    |___/
Visualize @pepecoineth courbe & Analyse FOMO               @sw6lnd   v1.0            """
    print(font)

if __name__ == "__main__":
    banner()




# Fetch PEPE cryptocurrency market data from CoinGecko
def get_pepe_data():
    url = 'https://api.coingecko.com/api/v3/coins/pepe/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': '30',  # Fetch data for the last 30 days
        'interval': 'daily'
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

# Convert the data to a pandas DataFrame
def process_data(data):
    prices = data['prices']
    timestamps = [datetime.utcfromtimestamp(item[0] / 1000) for item in prices]
    prices_in_usd = [item[1] for item in prices]

    df = pd.DataFrame({'Timestamp': timestamps, 'Price (USD)': prices_in_usd})
    return df

# Plot the data using matplotlib
def plot_pepe_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Timestamp'], df['Price (USD)'], label='PEPE Price')
    plt.title('PEPE Price Over Time (By @sw6lnd)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to run the script
if __name__ == "__main__":
    data = get_pepe_data()        # Step 1: Fetch data
    df = process_data(data)       # Step 2: Process data into DataFrame
    plot_pepe_data(df)            # Step 3: Visualize the data
