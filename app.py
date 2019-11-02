from flask import Flask, request, session, redirect, url_for, flash, g, abort, make_response, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        return render_template('layout.html')
    elif request.method == "POST":
        return "THIS IS A POST REQUEST"
    return "TEST"

@app.route("/login")
def login():
    return "LOGIN"
    
@app.route("/test")
def test():
    return render_template('choice.html')

@app.route("/time")
def time():
    return render_template('timeline.html')

@app.route("/board")
def board():
    return render_template('board.html')
    
if __name__ == "__main__":
    app.run()