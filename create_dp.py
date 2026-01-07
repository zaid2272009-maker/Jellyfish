import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table for menu items
c.execute('''
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
''')

# Insert some example menu items
c.execute("INSERT INTO menu (name, price) VALUES ('Classic Bubble Tea', 2.5)")
c.execute("INSERT INTO menu (name, price) VALUES ('Matcha Bubble Tea', 3.0)")
c.execute("INSERT INTO menu (name, price) VALUES ('Brown Sugar Milk Tea', 3.5)")

conn.commit()
conn.close()
print("Database created and menu items added!")

