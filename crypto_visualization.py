
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Fetch data from CoinGecko API
def fetch_crypto_data(coin_id='bitcoin', currency='usd', days=7):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        'vs_currency': currency,
        'days': days,
        'interval': 'daily'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Step 2: Process the data
def process_data(data):
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Step 3: Visualize the data
def plot_prices(df, coin_name='Bitcoin'):
    sns.set(style='darkgrid')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='timestamp', y='price', marker='o')
    plt.title(f'{coin_name} Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Run the program
if __name__ == "__main__":
    try:
        raw_data = fetch_crypto_data(coin_id='bitcoin', days=7)
        df = process_data(raw_data)
        plot_prices(df, coin_name='Bitcoin')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
