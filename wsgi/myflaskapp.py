from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! From C9.IO"

if __name__ == "__main__":
    app.run()

