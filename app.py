from flask import Flask, request, session, redirect, url_for, flash, g, abort, make_response, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('layout.html')

@app.route("/login")
def login():
    return "LOGIN"
    
if __name__ == "__main__":
    app.run()
