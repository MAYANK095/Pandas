import panda as pd 

df = pd.read_csv('C:/Users/iamay/Desktop/PY/data/iris.csv')
x = df['Species']
x.unique()
a=list(x)