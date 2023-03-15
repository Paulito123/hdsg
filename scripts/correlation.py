import pandas as pd
import numpy as np
import glob
import mplfinance as mpf
import matplotlib.pyplot as plt

# PARAMS
granularity = '1m'
pair_clean = 'agixusdt'
data_path = 'data'

# BINANCE
exch_str = 'bin'

# Define the path to the CSV files
path = f'{data_path}/{pair_clean}/{pair_clean}_{exch_str}_{granularity}_*.csv'

# Use glob to get a list of all CSV files in the path
all_files = glob.glob(path)

# Create an empty list to store each individual DataFrame
df_list = []

# Loop through each file in the list
for filename in all_files:
    # Read the CSV file into a DataFrame    , index_col='Timestamp', parse_dates=['Timestamp']
    df = pd.read_csv(filename)

    # Append the DataFrame to the list
    df_list.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
df_bin = pd.concat(df_list, axis=0, ignore_index=True)
# df_bin['Timestamp'] = pd.to_datetime(df_bin['Timestamp'], unit='ms')
# df_bin.set_index('Timestamp', inplace=True)


# KUCOIN
exch_str = 'kc'

# Define the path to the CSV files
path = f'{data_path}/{pair_clean}/{pair_clean}_{exch_str}_{granularity}_*.csv'

# Use glob to get a list of all CSV files in the path
all_files = glob.glob(path)

# Create an empty list to store each individual DataFrame
df_list = []

# Loop through each file in the list
for filename in all_files:
    # Read the CSV file into a DataFrame
    # df = pd.read_csv(filename, index_col='Timestamp', parse_dates=['Timestamp'], dtype={'Open':float, 'High':float, 'Low':float, 'Close':float, 'Volume':float})
    df = pd.read_csv(filename)
    
    # Append the DataFrame to the list
    df_list.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
df_kc = pd.concat(df_list, axis=0, ignore_index=True)
# df_kc['Timestamp'] = pd.to_datetime(df_kc['Timestamp'], unit='ms')
# df_kc.set_index('Timestamp', inplace=True)



# Merge data frames on time dimension
merged_df = pd.merge(df_bin, df_kc, on="Timestamp", how="outer", suffixes=("_bin", "_kc"))

# Create a figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# Plot exchange 1 data in the first subplot
axs[0].plot(merged_df["Timestamp"], merged_df["Close_bin"], label="Binance")
axs[0].set_title("Binance OHLCV Data")

# Plot exchange 2 data in the second subplot
axs[1].plot(merged_df["Timestamp"], merged_df["Close_kc"], label="Kucoin")
axs[1].set_title("Kucoin OHLCV Data")

# Add axis labels and legends
for ax in axs:
    ax.set_xlabel("Time (Unix Timestamp)")
    ax.set_ylabel("Price ($)")
    ax.legend()

fig.subplots_adjust(hspace=0.5)

# Show the plot
# plt.show()
plt.savefig("figure.png")



# # Combine the two DataFrames
# combined_df = pd.concat([df_bin, df_kc], axis=1)

# Create the candlestick chart with red and green candles
# mc = mpf.make_marketcolors(up='g', down='r')
# s = mpf.make_mpf_style(marketcolors=mc)
# mpf.plot(combined_df, type='candle', style=s)

# print(df_bin.head)
# print(df_kc.head)

# # calculate daily returns for both exchanges
# returns1 = df_bin['Close'].pct_change()
# returns2 = df_kc['Close'].pct_change()

# # calculate the drift
# drift = (returns1 - returns2).mean()

# print('The drift between the two data sets is:', drift)

# # calculate the correlation coefficient between the two data sets
# correlation = np.corrcoef(returns1, returns2)[0][1]

# print('The correlation between the two data sets is:', correlation)
