import sqlite3

query = """SELECT * FROM Student"""

conn = sqlite3.connect("seating.db")
cursor = conn.execute(query)
results = cursor.fetchall()

cursor.close()
conn.close()

print(results)
