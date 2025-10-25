from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! hey"

@app.route("/goodbye")
def goodbye():
    return "Goodbye, World!"

if __name__ == "__main__":
    app.run(debug=True)