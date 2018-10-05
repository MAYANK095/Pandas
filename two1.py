import pandas as pd
# import numpy as np
# import csv

df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/nyc_weather.csv")
print(df)
print(df.head())
print(df.tail())
print(df.columns)
print(df['EST'])
print(type(df['EST']))
print(df['Temperature']['EST'])
print(df['WindSpeedMPH'].min())
print(df['EST'][df['Temperature']==df['Temperature'].max()])
print(df['Temperature'].mean())
print(df['Temperature'].std())
print(df.describe())