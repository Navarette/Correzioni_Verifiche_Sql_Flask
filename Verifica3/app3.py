from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import pymssql
app = Flask(__name__)

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',user='navarette.arnold',password='xxx123##',database='navarette.arnold')

@app.route('/', methods=['GET'])
def home():
  return redirect(url_for('bestCustomers'))

@app.route('/bestCustomers', methods=['GET'])
def bestCustomers():
  return render_template('bestCustomers.html')
  

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=2223)