import pandas as pd
from bs4 import BeautifulSoup
import requests
import seaborn as sns

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

table = soup.find("table", {'class': "wikitable"}) ## read the table from the html file

newFile = pd.read_html(str(table))
dataFrame = newFile[0]

'''
print(dataFrame)
dataFrame.info()


mania = ["Ram", "Employees"]
nDataFrame = dataFrame[mania]
print(nDataFrame)
'''

catList = ["Employees"]

def findQuantile(money):
    quantile = dataFrame[money].quantile(.5)
    print(f"The Median Value of the {money} column is {quantile}")

findQuantile(catList)

def findAverage(money):
    average = dataFrame[money].mean()
    print(f"The Average Value of the {money} column is {average}")

findAverage(catList)