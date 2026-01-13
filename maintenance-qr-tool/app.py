"""
    Author: Christopher Gross
    Purpose: This is the "main" file which ties everything together.
    Version: 1.0
"""
from qr_engine import QrEngine
from menu import QrMenu
from flask import Flask
from flask import render_template

app = Flask(__name__) #create an instance of Flask
"""
menu_data = QrMenu.print_menu() #store data from the menu object
qr_engine = QrEngine()  #create an object of the QrEngine class
qr_image = qr_engine.generate_qr(**menu_data)   #create a qr code
qr_engine.save(qr_image)    #save the qr code
qr_engine.output()  #provide output to the user about the file we saved
"""
@app.route("/") #route for index
def index():
    return render_template("index.html")

#start Flask
if __name__=="__main__":
    app.run(debug=True)