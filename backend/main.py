from flask import Flask, request, render_template, jsonify
import pyodbc
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

server = os.getenv('SERVER_IP')
database = os.getenv('DATABASE_NAME')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

server ='146.148.86.108'
database ='myappdb'
username ='sqlserver'
password ='CLFA5D0A11@'


connection_string = f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes';



@app.route('/updateInventory', methods=['POST'])
def insert():
    data = request.json
    name = data['prod']
    quantity = data['qty']  # Expecting JSON data in the request body
    print(connection_string)
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PRODUCTS(Name, Quantity) VALUES(?, ?)", (name, quantity))
            return jsonify({ 'message':'Success'}), 200

    except Exception as e:
        return jsonify({'error':str(e)}), 500


@app.route('/getInventory', methods=['POST'])
def get_user_id():
    data = request.json
    product_name = data['product']
    try:
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Quantity from PRODUCTS where Name=(?)", (product_name, ))
            result = cursor.fetchall()
            print(result[0][0])
            return jsonify({ 'quantity' : result[0][0] }), 200

    except Exception as e:
        return jsonify({'error':str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6010, debug=True)