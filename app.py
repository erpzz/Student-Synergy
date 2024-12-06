# Lead Developer: Eric Paiz (Lead Developer, Database Architect, Documentation) Ligia Cerna (Lead Designer & Developer, Testing), Karla Cardenas (Database Developer, System Design), Scott Balzer (Communications expert, Systems Design, Documentation)


from flask import Flask, request, render_template, redirect, url_for, jsonify
import json
import os
import hashlib

app = Flask(__name__)

USER_FILE = os.path.join(os.getcwd(), 'users.json')

if not os.path.exists(USER_FILE):
    with open(USER_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    # Load users
    with open(USER_FILE, 'r') as f:
        users = json.load(f)

    # Check if user exists
    for user in users:
        if user['email'] == email:
            return jsonify({"error": "User already exists!"}), 400

    # Hash password and save new user
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': hashed_password
    }

    users.append(new_user)
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

    return jsonify({"message": "User successfully registered!"}), 200

@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')
@app.route('/forgot_password')
def forgot_password():
    return render_template('pwd.html')
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
