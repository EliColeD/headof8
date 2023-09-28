stocks = {"AAPL": 236.2, "DIS": 80.26, "GOOGL": 1215.71, "AMZN": 1731.92, "SQNFX": 24.80,
          "NTDOF": 66.09, "WBD": 89.52, "YAMCY": 49.75, "CHWY": 23.19, "NFLX": 282.93}

print('\nEnter Ticker Symbol (ex:Yamcy) type QUIT to stop')
query = ''

while True:
    query = input('\nInput: ').strip().upper()

    if query == 'QUIT':
        break

    if query in stocks:
        print(f"{query} has a stock price of {stocks[query]}")
    else:
        print(f'{query} was not found in database')
