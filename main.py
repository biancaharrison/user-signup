from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome_user():
    valid_username = request.form['username']
    valid_password = request.form['password']
    verified_password = request.form['password-verify']
    valid_email = request.form['email']


    if (not valid_username) or (valid_username.strip() == ""):
        error = "Please enter valid username"
        return redirect("/?error=" + error)

    if (not valid_password) or (valid_password.strip() == ""):
        error = "Please enter valid password"
        return redirect("/?error=" + error)

    if (not verified_password) or (verified_password.strip() == ""):
        error = "Please verify password"
        return redirect("/?error=" + error)

    if verified_password != valid_password:
        error = "Passwords do not match"        
        return redirect("/?error=" + error)

    return render_template('welcome.html', username=valid_username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html', error=encoded_error)

app.run()    