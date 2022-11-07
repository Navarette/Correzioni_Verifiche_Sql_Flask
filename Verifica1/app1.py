from flask import Flask,render_template,request
import pandas as pd
import pymssql
app = Flask(__name__)

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',user='navarette.arnold',password='xxx123##',database='navarette.arnold')

@app.route('/', methods=['GET'])
def home():
  return render_template('home1.html')

@app.route('/ricerca', methods=['GET'])
def ricerca():
  nome_Store = request.args['NomeStore']

  query = f"select first_name,last_name from Sales.stores  as ss inner join Sales.staffs as st on ss.store_id = st.store_id where store_name = '{nome_Store}' "
   
  df_store = pd.read_sql(query,conn)
  if df_store.values.tolist() == []:
    return render_template('error.html')
  else:
    return render_template('risultati1.html', nomiColonne = df_store.columns.values, dati = list(df_store.values.tolist()))

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=2222)