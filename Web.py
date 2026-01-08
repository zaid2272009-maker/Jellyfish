from flask import Flask, render_template, request, redirect
import sqlite3
import re  # for phone validation

app = Flask(__name__)

from flask import Response

@app.route('/google9d022a88b9b3a116.html')
def google_verify():
    return Response(
        "google-site-verification: google9d022a88b9b3a116.html",
        mimetype="text/html"
)

# Example bubble options
bubble_options = [
    {"name": "Tapioca"},
    {"name": "Popping Boba"},
    {"name": "Aloe Vera"},
    {"name": "Lychee Jelly"}
]

# Helper function to get DB connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/orders')
def view_orders():
    conn = get_db_connection()
    c = conn.cursor()

    # Join orders with drinks to show drink names instead of just IDs
    c.execute("""
        SELECT orders.id, orders.name, orders.phone, drinks.name, drinks.price, orders.bubbles
        FROM orders
        JOIN drinks ON orders.drink_id = drinks.id
        ORDER BY orders.id DESC
    """)
    all_orders = c.fetchall()
    conn.close()

    return render_template('orders.html', orders=all_orders)



@app.route('/full-menu')
def full_menu():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, name, price, description, image_filename FROM drinks")
    drinks = c.fetchall()
    conn.close()
    return render_template('full_menu.html', drinks=drinks)


@app.route('/', methods=['GET', 'POST'])
def home():
    conn = get_db_connection()
    c = conn.cursor()

    # Fetch drinks from your menu table
    c.execute("SELECT id, name, price FROM drinks")
    drinks = c.fetchall()  # list of Row objects

    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        phone = request.form['phone']  # new phone field
        drink_id = request.form['drink']
        bubbles = request.form['bubbles']

        # Validate phone format (simple check)
        if not re.match(r'^\+?\d{10,12}$', phone):
            conn.close()
            return "Invalid phone number format", 400

        # Insert the order
        c.execute(
            "INSERT INTO orders (name, phone, drink_id, bubbles) VALUES (?, ?, ?, ?)",
            (name, phone, drink_id, bubbles)
        )
        conn.commit()
        conn.close()
        return redirect('/')

    # GET request
    conn.close()
    return render_template('index.html', bubble_options=bubble_options, drinks=drinks)


if __name__ == "__main__":
    app.run(debug=True)

