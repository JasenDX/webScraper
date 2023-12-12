from flask import Flask, render_template, request
from webScrapper import *

app = Flask(__name__)

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
    nameEco = output["nameEco"]
    finalEco = runPrices("ama", nameEco)
    print(finalEco)
    return render_template('website.html', nameEco = nameEco, finalEco = finalEco)



if __name__ == "__main__":
    app.run()
