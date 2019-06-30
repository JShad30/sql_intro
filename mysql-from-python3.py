import os
import datetime
import pymysql

#Get username from Cloud9 workspace
#(Modify this variable if running on another environment)

username = os.getenv('C9_USER')

#Connect to the database
db = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    #If there was nothing in the brackets here then it would be printed in the terminal, but the 'cursors.DictCursor' has put the info regarding genres into a dictionary
    #If in dictionary form, it can then be used as a json file
    with db.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        #Note that the above will display a warning not an error if the table already exists
        for row in cursor:
            print(row)
finally: 
    #Close the connection, regardless of whether the above was successful
    db.close()