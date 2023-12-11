from tkinter import *
from main import writeToGui
from webScraper import *

m = Tk() #creates window
tracker = 0 #keeps track of whether eccomerce or stocks

#moves stock input out of range, moves ecomerce inputs in place, sets tracker
def selE():
    sInputL.place_configure(relx = 1, rely = 1)
    sInput.place_configure(relx = 1, rely = 1)

    eInputL.place(relx = 0.2, rely = 0.1)
    eInput.place(relx = 0.5, rely = 0.1)

    tracker = 1

#moves ecomerce input out of range, moves stock inputs in place, sets tracker
def selS():
    eInputL.place_configure(relx = 1, rely = 1)
    eInput.place_configure(relx = 1, rely = 1)

    sInputL.place(relx = 0.2, rely = 0.1)
    sInput.place(relx = 0.55, rely = 0.1)

    tacker = 2

#checks tracker, then unwraps the corresponding list (either ecomerce or stock) from webScrapper.py, and then assigns the data to output
def writeToOutput():
    print("output")
    if(tracker == 1):
        output.insert(f"Price: {getVars('ecomerce', 'gui')}")

        output.place_configure(relx = 0.2, rely = 0.2)

    elif(tracker == 2):
        output.insert(1, f"Price: {getVars('stocs','gui')}")

        output.place_configure(relx = 0.2, rely = 0.2)

def search():
    print("search")
    if(tracker == 1):
        runPrices("ama", (eInput.get()))
        writeToOutput()

    elif(tracker == 2):
        runStocks(sInput.get())
        writeToOutput()

m.title("Web Scraper")
m.geometry("1000x1000")
m.configure(bg = "gray20")

Label(m, text = "Bee & Mele's Hopefully Functioning Web Scraper!", font = ("Impact", 20), fg = "white", bg = "gray20").place(relx = 0.5, rely = 0.02, anchor = CENTER)

#Buttons that decide whether ecomerce or stocks
eButton = Button(m, text = "Ecomerce", bg = "gray20", fg = "white", font = ("Impact", 16), command = selE).place(relx = 0.2, rely = 0.05)
sButton = Button(m, text = "Stocks", bg = "gray20", fg = "white", font = ("Impact", 16), command = selS).place(relx = 0.7, rely = 0.05)
searchButton = Button(m, text = "Search", bg = "gray20", fg = "white", font = ("Impact", 16), command = search).place(relx = 0.5, rely = 0.17, anchor = CENTER)

#ecomerce Inputs
eInputL = Label(m, text = "Input What You Want To Search: ", bg = "gray20", fg = "white", font = ("Impact", 16))
eInput = Entry(m, bg = "gray20", fg = "white", font = ("Impact", 16))
#eInputL.place(relx = 0.2, rely = 0.1)
#eInput.place(relx = 0.5, rely = 0.1)

#Stocks Inputs
sInputL = Label(m, text = "Input What Stock You Want To Search: ", bg = "gray20", fg = "white", font = ("Impact", 16))
sInput = Entry(m, bg = "gray20", fg = "white", font = ("Impact", 16))
#sInputL.place(relx = 0.2, rely = 0.1)
#sInput.place(relx = 0.55, rely = 0.1)

#Output
Label(m, text = "OUTPUT", font = ("Impact", 16), fg = "white", bg = "gray20").place(relx = 0.5, rely = 0.24, anchor = CENTER)
output = Listbox(m, bg = "gray20", fg = "white", font = ("Impact", 16), width = 60)

output.place(relx = 0.2, rely = 0.27)

m.mainloop() 
