import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='liji', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Executes a SQL statement

#Creating table as per requirement
sql ='''CREATE TABLE Arokee.EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''

cursor.execute(sql)

# fetch all results
print(cursor.fetchall())

conn.close()
