from database.process_data import main as process_data_main

stock_symbol = 'AAPL'  # Example stock symbol
input_date = '2023-04-01'  # Example input date
backdate_years = 1 # default
process_data_main(stock_symbol, input_date=input_date)
