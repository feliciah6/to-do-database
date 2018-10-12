#!flask/Source/python
import mysql.connector
from mysql.connector import errorcode
from flask import Flask,jsonify
def mysql_conn():
    try:
     connection = mysql.connector.connect(host = 'localhost',
    	user='root',
    	password='mkulimas',
    	database='todo_list')

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    
    return connection

app = Flask('app')
@app.route('/')
def index():
	return 'Hello world its feliciah'

@app.route('/user',methods=['GET'])
def get_users():
  conn = mysql_conn()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM user")
  result = cursor.fetchall()

  return jsonify(result)




# app.run(debug=True, host='0.0.0.0', port=8080)
if   __name__ == '__main__':
	app.run(debug=True)