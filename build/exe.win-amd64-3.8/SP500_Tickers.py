ticker_string = open(
    'B:\Coding Projects\Robinhood_Helper_Tool\spy_tickers.txt', 'r')

SP500_ticker_string_list = []

for ticker in ticker_string:
    new_ticker = ticker.replace('\n', '')
    SP500_ticker_string_list.append(new_ticker)

# print(SP500_ticker_string_list)
