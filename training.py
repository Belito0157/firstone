import re
from flask import Flask, render_template, request, redirect
import csv



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:page_name>")
def pages(page_name):
    return render_template(page_name+".html")

def write_csv_file(data):
    with open('database.csv', newline="", mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])

@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv_file(data)
        return redirect("thank")
    else:
        return 'something went wrong'