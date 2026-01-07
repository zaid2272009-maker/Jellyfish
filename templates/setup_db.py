import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Create drinks table
c.execute("""
CREATE TABLE IF NOT EXISTS drinks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# Insert sample drinks
c.execute("INSERT OR IGNORE INTO drinks (id, name, price) VALUES (1, 'Classic Milk Tea', 3.5)")
c.execute("INSERT OR IGNORE INTO drinks (id, name, price) VALUES (2, 'Taro Bubble Tea', 4.0)")
c.execute("INSERT OR IGNORE INTO drinks (id, name, price) VALUES (3, 'Strawberry Smoothie', 4.5)")

# Create orders table
c.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    drink_id INTEGER NOT NULL,
    bubbles TEXT,
    FOREIGN KEY (drink_id) REFERENCES drinks(id)
)
""")

conn.commit()
conn.close()

