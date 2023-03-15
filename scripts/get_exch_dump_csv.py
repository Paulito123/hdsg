import ccxt
from ccxt import kucoin, binance
import pandas as pd
import time
import datetime

data_files_path = '/home/user/Data'

# set parameters
exch_str = 'bin'
if exch_str == 'bin':
    exchange = ccxt.binance()
elif exch_str == 'kc':
    exchange = ccxt.kucoin()
else:
    raise Exception
granularity = '1m'
pair = 'AGIX/USDT'
pair_clean = 'agixusdt'
data_path = 'data'
interval = 1440
rate_limit_sleep_time = 1
limit = 1000
ohlcv_data = []
start = True

# set start and end times for data retrieval
start_time = int(datetime.datetime.fromisoformat("2023-03-14T00:00:00+00:00").timestamp())
end_time = int(datetime.datetime.fromisoformat("2023-03-15T00:00:00+00:00").timestamp())
# print(f"{start_time} < {end_time}")
# print(f"start_time={datetime.datetime.fromtimestamp(start_time)} | end_time={datetime.datetime.fromtimestamp(end_time)}")
# print(f"start_time={datetime.datetime.fromtimestamp(start_time+1000)}")

# retrieve data in chunks of 1000 records per call
while start_time < end_time:
    print(f"{start_time} < {end_time} | start_time={datetime.datetime.fromtimestamp(start_time)}")

    data = exchange.fetch_ohlcv(pair, granularity, int(start_time * 1000), limit=limit)
    ohlcv_data += data
    
    if len(ohlcv_data) > interval and not start:
        rest = len(ohlcv_data) - interval
        print(f"rest={rest} | len(ohlcv)={len(ohlcv_data)}")
        
        new_ohlcv_data = ohlcv_data[interval:]
        ohlcv_data = ohlcv_data[:-rest]
        # convert data to pandas dataframe and set column names
        df = pd.DataFrame(ohlcv_data, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])

        # Convert first timestamp to datetime object for filename
        datetime_object = datetime.datetime.utcfromtimestamp(int(ohlcv_data[1][0]/1000))
        filename = f"{data_path}/{pair_clean}/{pair_clean}_{exch_str}_{granularity}_{datetime_object.strftime('%Y%m%d')}.csv"

        # write data to file
        df.to_csv(filename, index=False)

        # create new data list from rest of previous data list
        ohlcv_data = new_ohlcv_data
    
    start = False if start else False

    # Add x minutes to the datetime object
    dt = datetime.datetime.fromtimestamp(start_time)
    dt_new = dt + datetime.timedelta(minutes=limit)
    start_time = int(dt_new.timestamp())

    time.sleep(rate_limit_sleep_time) # pause for 1 second between requests to avoid rate limit

