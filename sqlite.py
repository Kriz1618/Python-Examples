import sqlite3

connection = sqlite3.connect('Local.db')
cur = connection.cursor()

# Create a table
# cur.execute('CREATE TABLE Product (p_id INTEGER PRIMARY KEY AUTOINCREMENTAL')

# Insert data
cur.execute("INSERT INTO Product(p_name, price, quantity) VALUES('Monitor', 1200, 32)")
cur.execute("INSERT INTO Product(p_name, price, quantity) VALUES('KeyBoard', 200, 2)")
cur.execute("INSERT INTO Product(p_name, price, quantity) VALUES('Mouse', 300, 1)")
cur.execute("INSERT INTO Product(p_name, price, quantity) VALUES('Camera', 100, 2)")

# Query Data
cursor = cur.execute("SELECT * FROM Product")
print(f"Cursosr {cursor}")
print("p_id \t p_name \t price \t quantity")
for item in cursor:
  print(f"{item[0]} \t {item[1]} \t {item[2]} \t {item[3]}")  

# Update Data
cur.execute("UPDATE Product SET quantity = quantity + (quantity *0.2)")
cur.execute("UPDATE Product SET price = price * 5 WHERE price < 600")

print("====================//====================")

cursor = cur.execute("SELECT * FROM Product")

for item in cursor:
  print(f"{item[0]} \t {item[1]} \t {item[2]} \t {item[3]}")  

cur.close()