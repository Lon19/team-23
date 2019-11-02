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
    
@app.route("/courses_list")
def courses_list():
    return render_template('courses_list.html')
if __name__ == "__main__":
    app.run()