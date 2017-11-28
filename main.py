from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def username():
    return render_template('signup.html', username=username)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html')

app.run()    