from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "OH LAWD IT WORKIN"

@app.route("/login")
def login():
    return "LOGIN"
if __name__ == "__main__":
    app.run()
