from flask import Flask, request, session, redirect, url_for, flash, g, abort, make_response, render_template, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def test():
    return render_template('choice.html')
    
@app.route("/courses_list")
def courses_list():
    return render_template('courses_list.html')

@app.route("/myboards")
def board():
    return render_template('board.html')

@app.route("/requirements")
def courses():
    from .scraping import get_requirements
    return get_requirements()

if __name__ == "__main__":
    app.run()
