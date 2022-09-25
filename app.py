from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Hi from focus</h1>"

if __name__=="__main__":
    app.run(port=5000)