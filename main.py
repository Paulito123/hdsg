import os
# import constant as c
import helper as h
from binance.client import Client





def full_load(binance_client, interval, ticker_list, mmyy_from):
    """

    :param binance_client:
    :param interval:
    :param ticker_list:
    :param mmyy_from:
    :return:
    """

    if interval == Client.KLINE_INTERVAL_1MINUTE:
        print("bam!")
        klines = binance_client.get_historical_klines("BNBBTC", interval, '1 Jan, 2022', '5 Jan, 2022')

        return klines
    else:
        print("Interval not supported!")
        return []


def main():
    ### API
    binance_api_key = os.getenv("BINANCE_API_KEY")
    binance_api_secret = os.getenv("BINANCE_API_SECRET")
    batch_size = 750
    timeframe = '1h'
    pairs = [
        # "ETHUSDT",
        # "XRPUSDT",
        "EOSUSDT",
        "LTCUSDT",
        # "ETCUSDT",
        # "DASHUSDT",
        # "ZECUSDT",
        # "XLMUSDT",
        # "XMRUSDT",
        # "BNBUSDT",
        # "LINKUSDT",
        # "TRXUSDT",
        # "ADAUSDT",
        # "IOTAUSDT"
    ]

    binance_client = Client(api_key=binance_api_key, api_secret=binance_api_secret)
    from_dt = '1 Jan, 2022'
    to_dt = '2 Jan, 2022'

    candles = full_load(binance_client, Client.KLINE_INTERVAL_1MINUTE, from_dt, to_dt)
    print(candles)

if __name__ == '__main__':
    main()
