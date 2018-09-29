#!flask/Source/python
import mysql.connector
from mysql.connector import errorcode
from flask import Flask

try:
 connection = mysql.connector.connect(host = 'localhost',
	user='',
	password='',
	database='todo_list')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  connection.close()

app = Flask('app')
@app.route('/')
def index():
	return 'Hello world its feliciah'



# app.run(debug=True, host='0.0.0.0', port=8080)
if   __name__ == '__main__':
	app.run(debug=True)