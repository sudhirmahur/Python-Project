# hey welcome to coding lover...
# i am here to learn and share my knowledge with you all

import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="******",database="users_data")
cursor=conn.cursor()
cursor.close()
conn.close()
print("Connection_Sucessfull")
