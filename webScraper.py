import requests
from bs4 import BeautifulSoup

#ecommerce var
ePrice = 0.0
	
#stock vars
sPrice = 0.0

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
	else:
		print("ERROR - could not connect to website")

def runStock(item):
	stocks = (f"https://www.marketwatch.com/investing/stock/{item}?mod=search_symbol") #stock website
	r = requests.get(stocks) #gets HTML of website

	if(r.status_code == 200): #checks if website is up
		soup = BeautifulSoup(r.content, 'html5lib')
		priceElement = soup.find("Open")
		soup.find('div', {'class': 'intraday__data'})
		
		sPrice = priceElement.text.strip()
	else:
		print("ERROR - could not connect to website")	

def runEbay(item):
	print("Ebay")
	ebay = "https://www.ebay.com/"


def runAMA(item):
	print("AMA")


#organizes the variables based on output type and website type and sends them either as a string or a list
def getVars(webType, outputType):
	if(outputType == "disk"):
		
		if(webType == "ecommerce"):
			return (f"{EPrice}")

		elif(webType == "stock"):
			return (f"{sPrice}")
		
	elif(outputType == "gui"):
		
		if(webType == "ecommerce"):
			return [ePrice]
			
		elif(outputType == "stock"):
			return [sPrice]

print(runStock("AMZN"))
