from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import pymssql
app = Flask(__name__)

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',user='navarette.arnold',password='xxx123##',database='navarette.arnold')

@app.route('/bestCustomers', methods=['GET'])
def bestCustomers():
   query = 'SELECT TOP 10 customers.customer_id, customers.first_name, customers.last_name ,SUM(list_price * quantity) as spesa_totale FROM sales.customers INNER JOIN sales.orders ON sales.customers.customer_id = sales.orders.customer_id INNER JOIN sales.order_items ON sales.order_items.order_id = sales.orders.order_id GROUP BY customers.customer_id, customers.first_name, customers.last_name ORDER BY SUM(list_price * quantity) DESC '
    #INNER JOIN sales.oder_items ON sales.orders.order_id = sales.order_items.order_id
   tabella = pd.read_sql(query,conn)
   return render_template('bestCustomers.html', nomiColonne = tabella.columns.values, dati = tabella.values)

@app.route("/totaleOrdini/<valore>")
def totaleOrdini(valore):
    query = f'SELECT * FROM sales.customers INNER JOIN sales.orders ON sales.customers.customer_id = sales.orders.customer_id WHERE customers.customer_id = {valore}'
    tabella = pd.read_sql(query,conn)
    return render_template("totaleOrdini.html", nomiColonne = tabella.columns.values, dati = tabella.values)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=2223)