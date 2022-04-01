import os
import constant as c
import helper as h
from binance.client import Client


def load_history(binance_client, interval, ticker_list, mmyy_from, mmyy_to=None):
    """
    Load a defined part of historic data for a given start date and a given list of tickers.
    If a to date is specified, data is loaded for all months between the given dates.
    Data is exported to files, one file for one month of data.
    :param binance_client:
    :param interval:
    :param ticker_list:
    :param mmyy_from:
    :param mmyy_to: Optional parameter if only a portion of the
    :return:
    """

    # TODO: include simple logging about what has been successfully loaded and what not.
    ### Check input
    if not(binance_client):
        print("ERROR: if binance_client:")

    if not(h.mmyy_valid_date(mmyy_from)):
        print("ERROR: if h.mmyy_validate(mmyy_from):")

    if mmyy_to and not(h.mmyy_validate(mmyy_to)):
        print("ERROR: if mmyy_to and h.mmyy_validate(mmyy_to):")

    if mmyy_to and not(h.mmyy_to_older_then_from(mmyy_from, mmyy_to)):
        print("ERROR:  if mmyy_to and not(h.mmyy_to_older_then_from(mmyy_from, mmyy_to)):")

    if interval in c.BINANCE_SUPPORTED_TFS:
        # TODO try catch block
        for ticker in ticker_list:
            mmyy_iter = h.mmyy_make_iterable_from_to(mmyy_from, mmyy_to)

            for mmyy in mmyy_iter:
                from_dt, to_dt = h.mmyy_date_slicer(mmyy)
                if to_dt and not(to_dt == ""):
                    klines = binance_client.get_historical_klines(ticker, interval, from_dt, to_dt)
                else:
                    klines = binance_client.get_historical_klines(ticker, interval, from_dt)

                fqfilename = f"{c.OUTPUT_DIR}/{h.create_filename(ticker, interval, mmyy)}"
                h.ohlcvn_response_to_csv(klines, fqfilename)

        return ['ok']
    else:
        print("Interval not supported!")
        return ['nok']


def main():
    ### API connection
    binance_api_key = os.getenv("BINANCE_API_KEY")
    binance_api_secret = os.getenv("BINANCE_API_SECRET")
    binance_client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

    ### Parameters
    pairs = [
        "ETHUSDT",
        "XRPUSDT",
        # "EOSUSDT",
        # "LTCUSDT",
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
    interval = Client.KLINE_INTERVAL_1MINUTE
    from_mmyy = '0122'
    to_mmyy = '0322'

    result = load_history(binance_client, interval, pairs, from_mmyy)
    print(result)

if __name__ == '__main__':
    main()
