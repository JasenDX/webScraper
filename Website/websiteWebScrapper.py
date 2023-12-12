import requests
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#ecommerce vars
ePrice = ""
	
#stock vars
sPrice = 0.0

#open website, finds price, returns relevant data
def runPrices(website, item):
		if(website == "all"): #runs both ebay and amazon and returns average price
			avgPrice = runEbay(item) + runAMA(item) 
			ePrice = (avgPrice / 2)
		
		if(website == "ebay"): #ebay
			ePrice = runEbay(item)

		if(website == "ama"): #ama
			ePrice = runAMA(item)
		print(ePrice + " Test")
		return getVars(ePrice)

def runStock(item):
	stocks = (f"https://www.marketwatch.com/investing/stock/{item}?mod=search_symbol") #stock website
	r = requests.get(stocks) #gets HTML of website

	if(r.status_code == 200): #checks if website is up
		#soup = BeautifulSoup(r.content, 'html.parser')
		soup = BeautifulSoup(r.content, 'html5lib')

		priceElement = soup.find('bg-quote', class_='value')


		#sPrice = 10.5
		sPrice = priceElement.text.strip()

		#print(getVars("stock", "disk"))

	else:
		return "ERROR - could not connect to website"

	return getVarsStock(sPrice)



def runAMA(item):
	ama = "https://www.amazon.com/"
	price = ""

	driver = webdriver.Chrome()
	driver.get(ama)

	driver.implicitly_wait(3)

	searchBar = driver.find_element(By.ID, "twotabsearchtextbox")
	searchBar.clear()
	searchBar.send_keys(item)
	searchBar.send_keys(Keys.RETURN)

	driver.implicitly_wait(3)

	firstResultText = driver.find_element(By.CSS_SELECTOR,"a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
	firstResultLink = firstResultText.get_attribute('href')

	driver.get(firstResultLink)

	driver.implicitly_wait(3)

	priceElementWhole = driver.find_element(By.CLASS_NAME, "a-price-whole")
	priceElementFraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
	price = (f"{priceElementWhole.text}.{priceElementFraction.text}")

	driver.close()
	print(price)
	return price


#organizes the variables based on output type and website type and sends them either as a string or a list
def getVarsStock(sPrice):#, open, pClose, volume, marketCap, beta, PERatio, EPS):
		return (f"Price: {sPrice}")#, Open: {open}, Close: {pClose}, Volume: {volume}, Market Cap: {marketCap}, Beta: {beta}, Per Ratio: {PERatio}, EPS: {EPS}")

def getVars(ePrice):#, shippingCost, discounts, shippingFrom, shippingTime):
			return (f"Price: {ePrice}")#, {shippingCost}, {discounts}, {shippingFrom}, {shippingTime}")
