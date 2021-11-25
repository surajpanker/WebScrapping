from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


#To configure webdriver to use Chrome browser, we have to set the path to chromedriver
import os 
from os.path import expanduser

User = expanduser("~")


#cldriver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Chrome(executable_path=r'C:/Users/sai/Videos/chromedriver')
#driver = webdriver.Chrome(executable_path=r'C:/Program Files/Google/Chrome/Application/chrome.exe')

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/oppo-a12-flowing-silver-64-gb/p/itmfc859cdf39e01?pid=MOBGYX8ETQGZZZ27&lid=LSTMOBGYX8ETQGZZZ27QDVWBW&marketplace=FLIPKART")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div',attrs={'class':'_1YokD2 _3Mn1Gg col-8-12'}):
    name=a.find('span', attrs={'class':'B_NuCI'})
    price=a.find('div', attrs={'class':'_30jeq3 _16Jk6d'})
    rating=a.find('div', attrs={'class':'_2d4LTz'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

#save into csv file
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')