import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='liji', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


# Executes a SQL statement


cursor.execute("select * from Arokee.employee order by age")

# fetch all results
print(cursor.fetchall())



conn.close()
