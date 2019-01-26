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
    #If there was nothing in the brackets here then it would be printed in the terminal, but the 'cursors.DictCursor' has put the info regarding genres into a dictionary
    #If in dictionary form, it can then be used as a json file
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = 'SELECT * FROM Genre;'
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally: 
    connection.close()