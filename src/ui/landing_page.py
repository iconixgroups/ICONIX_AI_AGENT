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
    createUser(username, password, email)
    return redirect(url_for('landing_page', message='SIGNUP_SUCCESS'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    loginUser(username, password)
    return redirect(url_for('landing_page', message='LOGIN_SUCCESS'))

if __name__ == '__main__':
    app.run(debug=True)

This Python code uses Flask, a web framework, to create the landing page for the ICONIX AI Agent web application. It defines routes for the landing page, signup, and login. The signup and login routes use POST methods to receive form data from the user, and call the createUser and loginUser functions from the user_management module to handle user creation and login. After successful signup or login, the user is redirected back to the landing page with a success message.
