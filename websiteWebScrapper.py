import requests
from bs4 import BeautifulSoup
import html5lib

#ecommerce vars
ePrice = 0.0
shippingCost = 0.0
discounts = 0.0
shippingFrom = ""
shippingTime = ""
	
#stock vars
sPrice = 0.0
open = 0.0
pClose = 0.0
volume = 0.0
marketCap = 0.0 
beta = 0.0
PERatio = 0.0
EPS = 0.0

#open website, finds price, returns relevant data
def runPrices(website, item):
	#ecommerce websites
	ebay = "https://www.ebay.com/"
	amazon = "https://www.amazon.com/ref=nav_logo"

	r = requests.get(website)
	soup = BeautifulSoup(r.content, 'html5lib')

	if(r.status_code == 200): #checks if website is up

		if(website == "all"): #all
			avgPrice = runEbay(item) + runAMA(item) 
			ePrice = (avgPrice / 2)
		
		if(website == "ebay"): #ebay
			ePrice = runEbay(item)

		if(website == "ama"): #ama
			ePrice = runAMA(item)

		getVars(ePrice, shippingCost, discounts, shippingFrom, shippingTime)

	else:
		print("ERROR - could not connect to website")

def runStock(item):
	stocks = (f"https://www.marketwatch.com/investing/stock/{item}?mod=search_symbol") #stock website
	r = requests.get(stocks) #gets HTML of website

	if(r.status_code == 200): #checks if website is up
		#soup = BeautifulSoup(r.content, 'html.parser')
		soup = BeautifulSoup(r.content, 'html5lib')

		priceElement = soup.find("Open")#soup.find('div', {'class': 'intraday__data'})


		openElement = soup.find('td', {'class': 'table__cell u-semi'})


		#sPrice = 10.5
		sPrice = priceElement.text.strip()
		open = openElement.text.strip()	

		#print(getVars("stock", "disk"))

	else:
		return "ERROR - could not connect to website"

	return getVars(sPrice, open, pClose, volume, marketCap, beta, PERatio, EPS)


def runEbay(item):
	print("Ebay")
	ebay = "https://www.ebay.com/"


def runAMA(item):
	print("AMA")


#organizes the variables based on output type and website type and sends them either as a string or a list
def getVars(sPrice, open, pClose, volume, marketCap, beta, PERatio, EPS):
		return (f"Price: {sPrice}, Open: {open}, Close: {pClose}, Volume: {volume}, Market Cap: {marketCap}, Beta: {beta}, Per Ratio: {PERatio}, EPS: {EPS}")

def getVars(ePrice, shippingCost, discounts, shippingFrom, shippingTime):
			return (f"{ePrice}, {shippingCost}, {discounts}, {shippingFrom}, {shippingTime}")


def getPrice():
	return sPrice
