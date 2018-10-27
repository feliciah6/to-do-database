import mysql.connector
from mysql.connector import errorcode




class Config:
  def __init__(self):
    self.connection=self.mysql_conn()
  def mysql_conn(self):
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

  def get_cursor(self):
    
      cursor = self.connection .cursor()

      return cursor