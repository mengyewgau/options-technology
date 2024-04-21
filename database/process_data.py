import pandas as pd
import yfinance as yf
from common.config import ENGINE as engine
from datetime import datetime, timedelta

def fetch_options_data(symbol, start_date):
    # Fetch stock data using yfinance
    stock = yf.Ticker(symbol)

    # Fetch options expiration dates within the given date range
    expirations = stock.options
    options_frames = []
    for date in expirations:
        if datetime.strptime(date, '%Y-%m-%d') >= start_date:
            opt = stock.option_chain(date)
            calls = opt.calls
            puts = opt.puts
            calls['type'] = 'call'
            puts['type'] = 'put'
            options_frames.append(calls)
            options_frames.append(puts)

    # Concatenate all data into a single DataFrame
    options_data = pd.concat(options_frames)
    options_data['timestamp'] = pd.to_datetime(options_data['lastTradeDate'])
    return options_data[['timestamp', 'strike', 'lastPrice', 'type']]

def resample_data(data, frequency):
    return data.set_index('timestamp').resample(frequency).agg({
        'lastPrice': 'mean'  # Aggregate last price by mean; adjust as needed
    }).reset_index()

def save_to_sql(data, table_name, sql_engine):
    data.to_sql(name=table_name, con=sql_engine, if_exists='append', index=False)

def main(symbol, input_date=None, backdate_years=1):
    if input_date:
        end_date = datetime.strptime(input_date, '%Y-%m-%d')
    else:
        end_date = datetime.now()
    start_date = end_date - timedelta(days=365 * backdate_years)

    print(f"Fetching options data for {symbol} from {start_date.date()} to {end_date.date()}")
    options_data = fetch_options_data(symbol, start_date)
    print(options_data)
    # List of candle time frames
    time_frames = {
        'daily': 'D',
        '60min': '60T',
        '30min': '30T',
        '5min': '5T',
        '1min': 'T'
    }

    for frame, freq in time_frames.items():
        print(f"Resampling data for {frame}")
        resampled_data = resample_data(options_data, freq)
        table_name = f"{symbol.lower()}_{frame}_options"
        print(f"Saving to SQL table: {table_name}")
        save_to_sql(resampled_data, table_name, engine)