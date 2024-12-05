import pandas as pd
from bs4 import BeautifulSoup
import requests
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

table = soup.find("table", {'class': "wikitable"}) ## read the table from the html file

newFile = pd.read_html(str(table)) 
dataFrame = newFile[0]

rows = table.find_all('tr')
data = []
for row in rows:
    cells = row.find_all('td')  # Find all cells in the row
    if cells:  # Skip empty rows
        data.append({
            'Name': cells[0].text.strip(),  # Replace with column names
            'Sector': cells[1].text.strip(),
            'Revenue (Millions)': cells[2].text.strip(),
            'Profit (Millions)': cells[3].text.strip(),
            'Employees': cells[4].text.strip(),
            'Geographic HQ': cells[5].text.strip()
        })

df = pd.DataFrame(data)
df.to_csv('companies', index=False)

companies = pd.read_csv('companies')

sns.histplot(df, kde=True)
plt.show()




'''
print(dataFrame)
dataFrame.info()


mania = ["Ram", "Employees"]
nDataFrame = dataFrame[mania]
print(nDataFrame)

emp = ["Employees"]
employees = dataFrame["Employees"]


def findQuantile(money):
    quantile = dataFrame[money].quantile(.5)
    print(f"The Median Value of the {money} column is {quantile}")

##findQuantile(emp)

def findAverage(money):
    average = dataFrame[money].mean()
    print(f"The Average Value of the {money} column is {average}")

##findAverage(emp)

##sns.histplot(employees, kde=True, color='red')
###plt.show()

'''