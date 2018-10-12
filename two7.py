import pandas as pd
df = pd.read_csv("C:/Users/iamay/Desktop/PY/data/example1.csv",
                 parse_dates=["day"])
df.set_index('day', inplace=True)
print(df)
dt=pd.date_range('01-01-2017','01-11-2017')
idx=pd.DatetimeIndex(dt)
df=df.reindex(idx)
print('\n',df)
new_df = df.fillna({
    #'temperature': 0,
    #'windspeed': 0,
    'event': 'Not Sure'
})
new_df=new_df.interpolate()
#new_df = df.fillna(method='ffill')
#new_df = df.fillna(method='bfill')
#new_df=df.fillna(method='bfill',axis='columns')
#new_df=df.fillna(method='ffill',axis='columns')
#new_df=df.fillna(method='bfill',axis='columns')
#new_df = df.fillna(method='ffill', limit=2)
#new_df=df.interpolate()
#new_df=df.dropna(how='all')
print('\n',new_df)