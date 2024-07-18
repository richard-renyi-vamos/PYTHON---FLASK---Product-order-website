from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        customer_name TEXT NOT NULL,
        customer_email TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def order_form():
    return render_template('order_form.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    product_name = request.form['product_name']
    quantity = request.form['quantity']
    customer_name = request.form['customer_name']
    customer_email = request.form['customer_email']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO orders (product_name, quantity, customer_name, customer_email)
    VALUES (?, ?, ?, ?)
    ''', (product_name, quantity, customer_name, customer_email))
    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
