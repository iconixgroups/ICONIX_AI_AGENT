```python
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from flask_mongoengine import MongoEngine
from mongoengine import Document, StringField, EmailField

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = MongoEngine(app)

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    user.save()
    return jsonify(message=SIGNUP_SUCCESS), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.objects.get(username=data['username'])
    if bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(message=LOGIN_SUCCESS, access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401

if __name__ == '__main__':
    app.run(debug=True)
```