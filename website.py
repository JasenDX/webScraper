from flask import Flask, redirect, url_for, render_template, request
from webScraper import *

app = Flask(__name__)
product = ""
webType = ""
sOrE = ""
gui = "gui"


    # Defining the home page of our site
@app.route("/")
def home():
    return render_template("website.html")
    
    
    

@app.route("/resultStock", methods=["POST", "GET"])
def resultStock():

    output = request.form.to_dict()
    print(output)
    name = output["name"]
    final = runStock(name)


    return render_template('website.html', name = name, final = final)

@app.route("/resultEcommerce", methods=["POST", "GET"])
def resultEcommerce():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    final = runPrices("all", name)

    return render_template('website.html', name = name, final = final)



def getProduct():
    return product



if __name__ == "__main__":
    app.run()
