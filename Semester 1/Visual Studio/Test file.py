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
    cells = row.find_all('td') 
    if cells: 
        data.append({
            'Name': cells[0].text.strip(), 
            'Sector': cells[1].text.strip(),
            'Revenue (Millions)': cells[2].text.strip(),
            'Profit (Millions)': cells[3].text.strip(),
            'Employees': cells[4].text.strip(),
            'Geographic HQ': cells[5].text.strip()
        })

df = pd.DataFrame(data)
df.to_csv('companies', index=False)

data = pd.read_csv('companies')

data['Revenue (Millions)'] = data['Revenue (Millions)'].str.replace('[$,]', '', regex=True).astype(int)
data['Employees'] = data['Employees'].str.replace('[$,]', '', regex=True).astype(int)
data['Profit (Millions)'] = data['Profit (Millions)'].str.replace('[$,]', '', regex=True).astype(int)

data.info()

sns.scatterplot(data=data, x='Revenue (Millions)', y='Employees')
plt.show()

print(dataFrame)
data.info()


mania = ["Name", "Employees"]
nData = data[mania]
###print(nData)

emp = ["Employees"]
employees = data["Employees"]


def findQuantile(money):
    quantile = data[money].quantile(.5)
    print(f"The Median Value of the {money} column is {quantile}")

##findQuantile(emp)

def findAverage(money):
    average = data[money].mean()
    print(f"The Average Value of the {money} column is {average}")

##findAverage(emp)

##sns.histplot(employees, kde=True, color='red')
###plt.show()

###findAverage("Employees")
###findAverage("Revenue (Millions)")

def revenuePerEmployee(company):
    if company in data['Name'].values:
        company_data = data[data['Name'] == company]
        ###print(company_data["Revenue (Millions)"])
        ###print(company_data["Employees"])
        revenue = (company_data["Revenue (Millions)"] * 1000000) / company_data["Employees"]
        print(f"The expected revenue generated per employee for {company} is {revenue} million.")
    else:
        print(f"Couldn't generate information for {company}.")

revenuePerEmployee("Walmart")
revenuePerEmployee("Amazon")
revenuePerEmployee("Saudi Aramco")

q = data["Revenue (Millions)"].mean()
a = data["Employees"].mean()
true = (q * 1000000) / a    
print(f"The Expected Revenue generated per employee of all companies listed is {true}")