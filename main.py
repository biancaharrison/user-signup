from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def welcome_user():
    username = request.form['username']
    password = request.form['password']
    verified_password = request.form['password-verify']
    user_email = request.form['email']

    username_error = ""
    password_error = ""
    verification_error = ""
    matching_error = ""
    email_error = ""

    if (not username) or (len(username.strip()) < 3):
        username_error = "Please enter a valid username"
        
    if (not password) or (len(password.strip()) < 8):
        password_error = "Please enter a valid password"

    if (not verified_password) or (verified_password.strip() == ""):
        verification_error = "Please verify password"

    if verified_password != password:
        matching_error = "Passwords do not match"        

    if user_email:
        if '@' not in user_email or '.' not in user_email:
            email_error = "Please enter a valid email"
        if (len(user_email) < 3) or (len(user_email) > 20):
            email_error = "Please enter a valid email"
                
    if username_error == "" and password_error == "" and verification_error == "" and matching_error == "" and email_error == "":
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup.html', username=username, 
        username_error=username_error,
        password_error=password_error,
        verification_error=verification_error,
        matching_error=matching_error,
        email_error=email_error,
        user_email=user_email)

    

@app.route("/")
def index():
    return render_template('signup.html')

app.run()    