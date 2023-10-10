from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from src.user_management import User, UserSchema
from flask_cors import CORS
from src.shared_dependencies import app, bcrypt, jwt, CORS

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user_schema = UserSchema()
    user = user_schema.load(data)
    user['password'] = bcrypt.generate_password_hash(user['password']).decode('utf8')
    result = User.create(user)
    if result:
        return jsonify({"message": "SIGNUP_SUCCESS"}), 201
    else:
        return jsonify({"message": "SIGNUP_FAILED"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.find_by_username(data['username'])
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=user['username'])
        return jsonify({"message": "LOGIN_SUCCESS", "access_token": access_token}), 200
    else:
        return jsonify({"message": "LOGIN_FAILED"}), 401

@app.route('/connectAI', methods=['POST'])
def connect_ai():
    data = request.get_json()
    user = User.find_by_username(data['username'])
    if user:
        user['ai_api_key'] = data['ai_api_key']
        User.update(user)
        return jsonify({"message": "AI_CONNECTED"}), 200
    else:
        return jsonify({"message": "AI_CONNECTION_FAILED"}), 400

if __name__ == '__main__':
    app.run(debug=True)