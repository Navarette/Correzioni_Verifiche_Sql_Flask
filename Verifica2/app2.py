from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import pymssql
app = Flask(__name__)

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',user='navarette.arnold',password='xxx123##',database='navarette.arnold')

@app.route('/', methods=['GET'])
def home():
  return redirect(url_for('infoUser'))

@app.route('/infoUser ', methods=['GET'])
def infoUser():
  return render_template('infoUser.html')

@app.route('/ricerca', methods=['GET'])
def ricerca():
  nome_cliente = request.args['NomeCliente']
  cognome_cliente = request.args['CognomeCliente']
  query = f"select * from Sales.customers where first_name = '{nome_cliente}' and last_name = '{cognome_cliente}'"
  df = pd.read_sql(query,conn)

  return render_template('ricerca.html',nomiColonne = df.columns.values, dati = list(df.values.tolist()))
if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=2223)