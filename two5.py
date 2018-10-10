import pandas as pd
df_stocks = pd.DataFrame({
    'tickers':['GOOGL', 'WMT', 'MSFT'],
    'price':[845, 65, 64],
    'pe':[30.37, 14.26, 30.97],
    'eps':[27.82, 4.61, 2.12]
})

df_weather = pd.DataFrame({
    'day':['1/1/17', '1/2/17', '1/3/17'],
    'temperature':[32, 35, 28],
    'event': ['Rain', 'Sunny', 'Snow']
})
with pd.ExcelWriter('C:/Users/iamay/Desktop/PY/data/darksecrets.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="Stocks")
    df_weather.to_excel(writer, sheet_name="Weather")