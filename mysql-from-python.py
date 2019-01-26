import os
import pymysql

#Get username from Cloud9 workspace
#(Modify this variable if running on another environment)

username = os.getenv('C9_USER')

#Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #Run a Query
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM Track;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally: 
    connection.close()