import requests
import json
import pandas as pd

# timeframes
tfs = ['1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']

# Define the endpoint URL
url = 'https://api.binance.com/api/v3/klines'

# Define the parameters for the request
params = {
    'symbol': 'BTCUSDT',
    'interval': '1m',
    'startTime': '1514764800000',  # Start time in milliseconds
    'endTime': '1514774800000',  # End time in milliseconds
    'limit': 1000  # Maximum number of data points to retrieve
}

# Send the request to the API and parse the response
response = requests.get(url, params=params)
data = json.loads(response.text)

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

# Convert the timestamp to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Convert the index to a datetime object if needed
df.index = pd.to_datetime(df.index, unit='ms')

# Resample the data to hourly frequency, aggregating using the mean
df_hourly = df.resample('1H').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last', 'volume': 'sum', 'close_time': 'last', 'quote_asset_volume': 'sum', 'num_trades': 'sum', 'taker_buy_base_asset_volume': 'sum', 'taker_buy_quote_asset_volume': 'sum', 'ignore': 'last'})

# Print the first few rows of the resampled DataFrame
print(df_hourly.head())