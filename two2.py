import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/iamay/Desktop/PY/data/iris.csv")
print("Sepal length min",df['SepalLengthCm'].min())
print("Sepal length mean",df['SepalLengthCm'].mean())
print("Sepal length max",df['SepalLengthCm'].max())
print("Sepal width min",df['SepalWidthCm'].min())
print("Sepal width mean",df['SepalWidthCm'].mean())
print("Sepal width max",df['SepalWidthCm'].max())
print("Petal length min",df['PetalLengthCm'].min())
print("Petal length mean",df['SepalLengthCm'].mean())
print("Petal length max",df['SepalLengthCm'].max())
print("Petal width min",df['PetalWidthCm'].min())
print("Petal width mean",df['PetalWidthCm'].mean())
print("Petal width max",df['PetalWidthCm'].max())
x=df['SepalLengthCm']
y=df['PetalLengthCm']
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.scatter(x, y)
plt.show()