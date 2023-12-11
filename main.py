from datetime import datetime
from webScraper import getVars

def saveToDisk(webType):
	if(webType == "ecommerce"):
		with open("eTextData.txt", "w") as file:
			file.write(f"{datetime.today()}: {getVars('ecommerse', 'disk')}")
												
	elif(webType == "stocks"):
		with open("sTextData.txt", "w") as file:
			file.write(f"{datetime.today()}: {getVars('stock', 'disk')}")

	else:
		print("ERROR - printing to Disk")

def writeToGui(webType):
	if((webType == "ecommerce") or (webType == "stock")):
		return getVars(webType, "gui")
	else:
		print("ERROR - could not write to GUI")

print(writeToGui('stock'))