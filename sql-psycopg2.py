import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object (array) of the database
cursor = connection.cursor()

# Query 1 - select all records from Artist table
cursor.execute('SELECT * FROM "artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)