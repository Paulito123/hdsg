# Historic Data Set Gatherer
### *- Only for Binance*

Historic Data Set Gatherer (HDSG) aims to do what the 
name implies, to gather historic OHCL data from 
Binance and Kucoin. 

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
> me a favor and create it with my referral code. 
> Thanks! :)
> [Create Binance account](https://accounts.binance.me/en/register?ref=11263187)


## What to do first
Copy .env.secret.dev and name it .env.secret.prod and
add your key and secret. 
```python
BINANCE_API_KEY=your-api-key-goes-here
BINANCE_API_SECRET=your-secret-goes-here
```
Install the requirements:
```sh
$ pip install -r requirements.txt
```

## How to operate

If you don't want to use environment variables, you can
just add your keys in config.py. Replace the "not_defined"
string with your key and secret.
```python
BINANCE_API_SECRET="not_defined"
BINANCE_API_KEY="not_defined"
```
Don't forget to update the destination directory in the 
config.py file.
```python
OUTPUT_DIR="/home/user/Data"
```
Once you are set to go, adjust the run parameters to your
liking in the **config.py** file and run the 
**main.py** file.
```python
PAIRS="ETHUSDT,BTCUSDT"
INTERVAL="1m"
FROM_MMYY="0122"
TO_MMYY=""
```
Some additional info about what is expected in the 
config.py file:
- **Don't change the value** of BINANCE_SUPPORTED_TFS.
- PAIRS are separated by a comma and have **no spaces** 
between, before or after them.
- All the possible values for intervals can be found in
the config.py file in the list named 
`BINANCE_SUPPORTED_TFS`.
- **Respect the date format** "mmyy" for the FROM_MMYY 
and TO_MMYY parameters. When TO_MMYY is left **empty**, 
TO_MMYY is automatically set to current month meaning 
all data is fetched from the FROM_MMYY until today.

## License

MIT

**Free Software, Hell Yeah!**

## TODO
- Get minute candles from Binance and Kucoin for several pairs that trade on both exchanges


# Data analysis
## TODO:
- Find out the correlation between trading pairs that exists on Binance and Kucoin, e.g. USDTAGIX, USDTBTC.
