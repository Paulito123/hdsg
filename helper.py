import re
import pandas as pd
from datetime import date, datetime, timedelta


def mm_yy_date_slicer(date_str):
    """Return start and end point for given date in mm-yy format
       :param date_str: date in mmyy format, i.e. "1222" or "0108".
    """
    # Check if date is well-formed
    today = date.today()
    check = re.match("^(0[1-9]|1[0-2])\/?([0-9]{2})$", date_str)

    # Initialize output
    start = ""
    end = ""

    if check:
        # Check if date is in the future
        dt_check = datetime.strptime(date_str, "%m%y")
        if dt_check.date() <= today:

            # Determine the start date string
            datetime_object = datetime.strptime(date_str[0:2], "%m")
            mo = datetime_object.strftime("%b")
            yyyy = f"20{date_str[2:]}"
            start = f'1 {mo}, {yyyy}'

            # Determine the end date string.
            mm = int(date_str[0:2])
            if mm == today.month:
                pass
            elif mm == 12:
                end = f"1 Jan, {int(yyyy)+1}"
            else:
                mm1 = int(date_str[0:2]) + 1
                datetime_object = datetime.strptime(f"{mm1}", "%m")
                mo1 = datetime_object.strftime("%b")
                end = f'1 {mo1}, {yyyy}'
        else:
            # print(f'date in the future! > {date_str}')
            return "", ""
    else:
        # print(f'date malformed! > {date_str}')
        return "", ""

    return start, end


def create_filename(ticker, interval, mmyy, ):


    return 1


def ohlcvn_response_to_csv(response, fqfilename):
    """
    :param response: A collection representing candlesticks with some additional info.
        Example:
        [
          [
            1499040000000,      // Open time
            "0.01634790",       // Open
            "0.80000000",       // High
            "0.01575800",       // Low
            "0.01577100",       // Close
            "148976.11427815",  // Volume
            1499644799999,      // Close time
            "2434.19055334",    // Quote asset volume
            308,                // Number of trades
            "1756.87402397",    // Taker buy base asset volume
            "28.46694368",      // Taker buy quote asset volume
            "17928899.62484339" // Ignore.
          ]
        ]
    :param file_dir: Directory in which the csv must be stored
    :param fqfilename: The fully qualified filepath and filename of the file in which data needs to be written
    :return: Status message of the operation
    """
    # Write collection to csv

    df = pd.DataFrame(data=response,
                      columns=['ts', 'o', 'h', 'l', 'c', 'v', 'ct', 'qav', 'nt', 'tbb', 'tbq', 'ign'])
    df = df.drop(['ct', 'qav', 'tbb', 'tbq', 'ign'], axis=1)
    df.to_csv(fqfilename, encoding='utf-8', index=False, header=False)

    return 1


if __name__ == '__main__':
    # print(mm_yy_date_slicer("1218"))

    response = [[1640995200000, '0.01106700', '0.01107700', '0.01106200', '0.01107600', '49.83000000', 1640995259999, '0.55154822', 59, '16.86600000', '0.18675310', '0'],
                [1640995260000, '0.01107600', '0.01107800', '0.01107000', '0.01107700', '61.18200000', 1640995319999, '0.67752268', 80, '31.72800000', '0.35134498', '0'],
                [1640995320000, '0.01107800', '0.01107800', '0.01107100', '0.01107300', '59.16000000', 1640995379999, '0.65513704', 47, '20.22300000', '0.22394926', '0']]
    fqfilename = '/home/user/Data/bla.txt'
    ohlcvn_response_to_csv(response, fqfilename)

# if __name__ == '__main__':
#     dt = datetime(2016, 1, 31)
#     print((dt.replace(day=1) + timedelta(days=32)).replace(day=1))