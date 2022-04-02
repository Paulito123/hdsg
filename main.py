import os
import constant as c
import helper as h
from binance.client import Client


def load_history(binance_client, interval, ticker_list, mmyy_from, mmyy_to=None):
    """
    Load a defined part of historic data for a given start date and a given list of tickers.
    If a to date is specified, data is loaded for all months between the given dates.
    Data is exported to files, one file for one month of data.
    :param binance_client: a binance client instance
    :param interval: interval of fetched ohcl-data
    :param ticker_list: a list of binance tickers
    :param mmyy_from: start date for data fetch in mmyy format
    :param mmyy_to: optional end date for data fetch in mmyy format
    :return: 1 (success) or 0 (error)
    """

    # Check input
    if not binance_client:
        mess = "ERROR: binance client not set"
        print(mess)
        return mess

    if not h.mmyy_valid_date(mmyy_from):
        mess = "ERROR: from_date malformed!"
        print(mess)
        return mess

    if mmyy_to and not h.mmyy_valid_date(mmyy_to):
        mess = "ERROR: to_date malformed!"
        print(mess)
        return mess

    if mmyy_to and not(h.mmyy_to_older_then_from(mmyy_from, mmyy_to)):
        mess = "ERROR: to_date incorrect!"
        print(mess)
        return mess

    if interval in c.BINANCE_SUPPORTED_TFS:
        file_counter = 0
        for ticker in ticker_list:
            mmyy_iter = h.mmyy_make_iterable_from_to(mmyy_from, mmyy_to)

            for mmyy in mmyy_iter:
                from_dt, to_dt = h.mmyy_date_slicer(mmyy)

                try:
                    if to_dt and not(to_dt == ""):
                        klines = binance_client.get_historical_klines(ticker, interval, from_dt, to_dt)
                    else:
                        klines = binance_client.get_historical_klines(ticker, interval, from_dt)
                except:
                    print("ERROR: Issue when fetching data from Binance")
                    continue

                fqfilename = f"{c.OUTPUT_DIR}/{h.create_filename(ticker, interval, mmyy)}"
                res = h.ohlcvn_response_to_csv(klines, fqfilename)
                print(res)

                if res[0:7] == "SUCCESS":
                    file_counter = file_counter + 1

        print(f"{file_counter} files have been created!")
        return 1
    else:
        print("Something went wrong. Call 911!")
        return 0


def main():
    # API connection
    # Uncomment next two lines if key is in constants.py
    # binance_api_key = c.BINANCE_API_KEY
    # binance_api_secret = c.BINANCE_API_SECRET
    # Comment next two lines if key is in constants.py
    binance_api_key = os.getenv("BINANCE_API_KEY")
    binance_api_secret = os.getenv("BINANCE_API_SECRET")
    # Create Binance client object
    binance_client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

    # Parameters
    pairs = [
        "ETHUSDT",
        "XRPUSDT"
    ]
    interval = Client.KLINE_INTERVAL_1MINUTE
    from_mmyy = '0122'
    to_mmyy = None

    load_history(binance_client, interval, pairs, from_mmyy, to_mmyy)


if __name__ == '__main__':
    main()


# TODO: Use a config file instead of constant.py
# TODO: make a testcase for all functions in helper file
# TODO: use a class instead of plain script