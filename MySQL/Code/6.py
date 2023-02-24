import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='liji', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Get values from user
name = "Ram"
lname = "Sharma"
age = "26"
sex = 'M'
income = "20000"

# Executes a SQL statement

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO Arokee.EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
   VALUES (%s, %s, %s, %s, %s)"""

# insert multiple records
data = [('Krishna', 'Sharma', 19, 'M', 2000), ('Raj', 'Kandukuri', 20, 'M', 7000),
('Ramya', 'Ramapriya', 25, 'F', 5000),('Mac', 'Mohan', 26, 'M', 2000)]

# execute many sql statements
cursor.executemany(sql, data)

conn.commit()

cursor.execute("select * from Arokee.employee")

# fetch all results
print(cursor.fetchall())



conn.close()
