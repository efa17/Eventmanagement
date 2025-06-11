from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# Create SQLite DB and table if not exists
def init_db():
    conn = sqlite3.connect('registrations.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            fullName TEXT NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL,
            semester TEXT NOT NULL,
            year TEXT NOT NULL,
            club TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Initialize DB on app start

# Serve your frontend (index.html)
@app.route('/')
def index():
    return render_template('register.html')  # Make sure index.html is inside 'templates/' folder

# Receive and save form data
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        email = data.get('email')
        full_name = data.get('fullName')
        phone = data.get('phone')
        department = data.get('department')
        semester = data.get('semester')
        year = data.get('year')
        club = data.get('club')

        # Basic validation
        if not all([email, full_name, phone, department, semester, year, club]):
            return jsonify({'status': 'error', 'message': 'Missing required fields.'}), 400

        conn = sqlite3.connect('registrations.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO registrations (email, fullName, phone, department, semester, year, club)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (email, full_name, phone, department, semester, year, club))
        conn.commit()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Registration successful!'}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({'status': 'error', 'message': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
