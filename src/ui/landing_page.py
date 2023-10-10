from flask import Flask, render_template, request, redirect, url_for
from src.user_management import createUser, loginUser

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    try:
        createUser(username, password, email)
    except Exception as e:
        return redirect(url_for('landing_page', message=str(e)))
    return redirect(url_for('landing_page', message='SIGNUP_SUCCESS'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        loginUser(username, password)
    except Exception as e:
        return redirect(url_for('landing_page', message=str(e)))
    return redirect(url_for('landing_page', message='LOGIN_SUCCESS'))

if __name__ == '__main__':
    app.run(debug=True)