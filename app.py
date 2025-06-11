from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)

# Initialize SQLite DB
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

# Call DB init
init_db()

# Route to serve your form (place register.html inside "templates" folder)
@app.route('/')
def form_page():
    return render_template('register.html')  # ✅ NOT 'payment.html'


# Route to handle form submission
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

        # Simple validation
        if not all([email, full_name, phone, department, semester, year, club]):
            return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

        # Save to DB
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
        return jsonify({'status': 'error', 'message': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
