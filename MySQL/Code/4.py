import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='liji', host='127.0.0.1')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Executes a SQL statement

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO Arokee.EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

cursor.execute(sql)

conn.commit()

cursor.execute("select * from Arokee.employee")

# fetch all results
print(cursor.fetchall())

conn.close()
