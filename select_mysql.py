import mysql.connector

# Open database connection
db = mysql.connector.connect(user="root",password="",host="localhost",database="db1")


# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMP \
       WHERE INCOME > 1000"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print("no of rows are",cursor.rowcount) 
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()
