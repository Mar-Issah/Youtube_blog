from flask import request, jsonify
from .models import User
from . import app, db

@app.route('/', methods=['GET'])
def sign():
    return "hello"

# Route for user sign-up
@app.route('/signup', methods=['POST'])
def signup():
    # Get data from request
    data = request.get_json()

    # Check if username and email are provided
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Check if the username or email already exists
    if User.query.filter_by(username=data['username']).first() is not None:
        return jsonify({'message': 'Username is already taken'}), 400
    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'Email is already registered'}), 400

    # Create a new user instance
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User signed up successfully'}), 201



@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        return jsonify({"message": "Login successful", "username": user.username}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401
