import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#ecommerce var
ePrice = ""
	
#stock var
sPrice = ""

#open website, finds price, returns relevant data
def runPrices(website, item):
	if(r.status_code == 200): #checks if website is up

		if(website == "all"): #runs both ebay and amazon and returns average price
			avgPrice = runEbay(item) + runAMA(item) 
			ePrice = (avgPrice / 2)
		
		if(website == "ebay"): #ebay
			ePrice = runEbay(item)

		if(website == "ama"): #ama
			ePrice = runAMA(item)
	else:
		print("ERROR - could not connect to website")

def runStock(item):
	stocks = (f"https://www.marketwatch.com/investing/stock/{item}?mod=search_symbol") #stock website
	r = requests.get(stocks) #gets HTML of website

	if(r.status_code == 200): #checks if website is up
		soup = BeautifulSoup(r.content, 'html.parser')
        # Find the element containing the stock price
		priceElement = soup.find('bg-quote', class_='value')

        # Extract the stock price from the element
		sPrice = priceElement.text.strip()

		return sPrice

	else:
		print("ERROR - could not connect to website")	

def runEbay(item):
	ebay = "https://www.ebay.com/"
	price = ""

	driver = webdriver.Chrome()
	driver.get(ebay)

	searchBar = driver.find_element(By.NAME, "_nkw")
	searchBar.clear()
	searchBar.send_keys(item)
	searchBar.send_keys(Keys.RETURN)

	driver.implicitly_wait(3)
	
	firstResultText = driver.find_element(By.CSS_SELECTOR, "a.s-item__link")
	firstResultLink = firstResultText.get_attribute('href')

	print(firstResultLink)
	
	driver.get(firstResultLink)

	driver.implicitly_wait(3)

	priceElement = driver.find_element(By.CLASS_NAME, "ux-textspans")
	price = priceElement.text

	return price
	
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

	return price


#organizes the variables based on output type and website type and sends them either as a string or a list
def getVars(webType, outputType):
	if(outputType == "disk"):
		
		if(webType == "ecommerce"):
			return (f"{EPrice}")

		elif(webType == "stock"):
			return (f"{sPrice}")
		
	elif(outputType == "gui"):
		
		if(webType == "ecommerce"):
			return ePrice
			
		elif(outputType == "stock"):
			return sPrice

#print(runStock("AMZN"))
#print(runEbay("ssd"))
#print(runAMA("computer"))