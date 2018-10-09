# import xlrd
import pandas as pd 


def convert_people_cell(cell):
    if cell == "n.a.":
        return 'Sam Walton'
    return cell


def convert_price_cell(cell):
    if cell == "n.a.":
        return 50
    return cell


df = pd.read_excel("C:/Users/iamay/Desktop/PY/data/stock_data.xlsx", converters={'people':convert_people_cell, 'price':convert_price_cell})
print(df)