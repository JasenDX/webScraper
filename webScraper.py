import requests
from bs4 import BeautifulSoup

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
			print("Both')
			

		if(website == "ebay"): #ebay
			print ("ama")

		if(website == "ama"): #ama
			print ("fMarket")
	else:
		print("ERROR - could not connect to website")

def runStock(item):
	stocks = (f"https://www.marketwatch.com/investing/stock/{item}?mod=search_symbol") #stock website
	r = requests.get(stocks) #gets HTML of website

	if(r.status_code == 200): #checks if website is up
		soup = BeautifulSoup(r.content, 'html5lib')
		
		priceElement = soup.find("Open")#soup.find('div', {'class': 'intraday__data'})


		openElement = soup.find('td', {'class': 'table__cell u-semi'})



		sPrice = priceElement.text.strip()
		open = openElement.text.strip()	

		print(sPrice)

		#print(getVars("stock", "disk"))

	else:
		print("ERROR - could not connect to website")	

def runEbay():
	print("Ebay")
	ebay = "https://www.ebay.com/"


def runAMA():
	print("AMA")


#organizes the variables based on output type and website type and sends them either as a string or a list
def getVars(webType, outputType):
	if(outputType == "disk"):
		
		if(webType == "ecommerce"):
			return (f"{EPrice}, {shippingCost}, {discounts}, {shippingFrom}, {shippingTime}")

		elif(webType == "stock"):
			return (f"{sPrice}, {open}, {pClose}, {volume}, {marketCap}, {beta}, {PERatio}, {EPS}")
		
	elif(outputType == "gui"):
		
		if(webType == "ecommerce"):
			return [ePrice, shippingCost, discounts, shippingFrom, shippingTime]
			
		elif(outputType == "stock"):
			return [sPrice, open, pClose, volume, marketCap, beta, PERatio, EPS]

print(runStock("AMZN"))
