#!flask/Source/python
from flask import Flask,jsonify,request
from config import Config

config = Config()
cursor =config.get_cursor()


app = Flask('app')
@app.route('/')
def index():
	return 'Hello world its feliciah';

@app.errorhandler(404)
def page_n0t_found(e):
  result = {
  "statusCode":404,
  "status":"failed",
  "message":"Url not found"

  }
  return jsonify(result)



@app.route('/user',methods=['GET'])
def get_users():
  
  cursor.execute("SELECT * FROM user")
  result = cursor.fetchall()

  return jsonify(result)


@app.route('/register',methods=['POST'])
def register_user():
  result = request.get_json()

  # Get data from the request object
  name = result['name']
  email = result['email']
  password = result['password']

  #insert data to the table
  query = "INSERT INTO user VALUES (%s, %s, %s, %s,NOW())"
  values = (3, name, email, password)
  cursor.execute(query, values)

  return jsonify(result)


# app.run(debug=True, host='0.0.0.0', port=8080)
if   __name__ == '__main__':
	app.run(debug=True)