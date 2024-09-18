
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_top_cryptocurrencies(limit=10):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': str(limit),
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '49b788e9-ba30-40da-90b1-9fd383279dc9',
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    return data['data']

def format_data(cryptocurrencies):
    formatted_data = []
    for crypto in cryptocurrencies:
        formatted_data.append({
            'Nome': crypto['name'],
            'Símbolo': crypto['symbol'],
            'Preço': f"${crypto['quote']['USD']['price']:.2f}",
            '1h %': f"{crypto['quote']['USD']['percent_change_1h']:.2f}%",
            '24h %': f"{crypto['quote']['USD']['percent_change_24h']:.2f}%",
            '7d %': f"{crypto['quote']['USD']['percent_change_7d']:.2f}%",
            'Market Cap': f"${crypto['quote']['USD']['market_cap']:.0f}",
            'Volume(24h)': f"${crypto['quote']['USD']['volume_24h']:.0f}",
            'Circulando': f"{crypto['circulating_supply']:.0f} {crypto['symbol']}"
        })
    return formatted_data

def display_data(data):
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

def main():
    cryptocurrencies = get_top_cryptocurrencies()
    formatted_data = format_data(cryptocurrencies)
    display_data(formatted_data)

if __name__ == "__main__":
    main()
