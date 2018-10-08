# reading data from csv format
import pandas as pd
'''df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv")
print(df, '\n\n')
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv", skiprows=1)
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv", header=1)
print(df, '\n\n')
print(df)
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv", header=None, names=["Tickers", "EPS", "Revenue", "People"])
print('\n\n', df)
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv", header=None, names=["Tickers", "EPS", "Revenue", "People"], nrows=2)
print('\n\n', df)
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv", na_values=["n.a.", "not available"])
print(df, '\n\n')'''
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv", na_values={
                 "eps": ["not available"], "revenue": ["-1"], "people": ["n.a.","not available"]})
print(df)
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/stock_data.csv")
df.to_csv("C:/Users/iamay/Desktop/PY/data/harambe.csv",index=False)