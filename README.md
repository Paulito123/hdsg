# Historic Data Set Gatherer
### *- Only for Binance*

Historic Data Set Gatherer (HDSG) aims to do what the 
name implies, to gather historic OHCL data from 
exchanges, currently only Binance. 

- Configure the timeframe, download location and list of tickers
- Run the program
- Dump data into data files from which they can be processed further

## Features

- It's simple!
- Fetch data from Binance.
- Dump data in csv files for further usage.
- Each data file has 1 month of data, regardless the timeframe.
- More features yet to be developed...

> A Binance account and API key and secret are required 
> to get the data. If you don't have an account yet, do 
> me a favor anc create it with my referral code. 
> Thanks! :)
> [Create Binance account](https://accounts.binance.me/en/register?ref=11263187)


## Usage

If you are using Linux and you like your keys to
be defined as environment variables, add your key
and secret to env.sh and make it executable. Then
go to the project directory and execute env.sh
```sh
~$ echo "Don't forget to add your key and secret to end.sh"
~$ cd /<path to...>/hdsg
../hdsg$ chmod +x env.sh
../hdsg$ sh env.sh
```
Install the requirements:
```sh
$ pip install -r requirements.txt
```
Install the requirements:
```sh
$ pip install -r requirements.txt
```
If you don't want to use environment variables, you can
just add your key in constants.py. But you will need to
comment 2 lines and uncomment 2 other lines in the
main.py file, as indicated in the code.
```sh
## Uncomment next two lines if key is in constants.py
# binance_api_key = c.BINANCE_API_KEY
# binance_api_secret = c.BINANCE_API_SECRET
## Comment next two lines if key is in constants.py
binance_api_key = os.getenv("BINANCE_API_KEY")
binance_api_secret = os.getenv("BINANCE_API_SECRET")
```
Update the data directory in the constant.py file.
```
OUTPUT_DIR = "/home/user/Data"
```
In the main file, you can play with the parameters when
running main.py.
```
# Parameters
pairs = ["ETHUSDT", "XRPUSDT"]
interval = Client.KLINE_INTERVAL_1MINUTE
from_mmyy = '0122'
to_mmyy = None
```

## License

MIT

**Free Software, Hell Yeah!**