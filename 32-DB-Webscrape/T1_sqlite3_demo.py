import sqlite3

# 1. Connect to (or create) the database
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
print("Connected to SQLite database.")

# 2. Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
print("Table 'users' created.")

# 3. Insert some data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
conn.commit()
print("Inserted Alice and Bob.")

# 4. Show all data
cursor.execute("SELECT * FROM users")
print("Current users:", cursor.fetchall())

# 5. Update (modify) a row
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
conn.commit()
print("Updated Alice's age to 31.")

# 6. Show all data again
cursor.execute("SELECT * FROM users")
print("After update:", cursor.fetchall())

# 7. Delete a row
cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
conn.commit()
print("Deleted Bob.")

# 8. Show final data
cursor.execute("SELECT * FROM users")
print("Final users:", cursor.fetchall())

# 9. Close the connection
conn.close()
print("Connection closed.")
