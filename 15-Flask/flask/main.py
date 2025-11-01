from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<html><body><h1>Hello, World! hey</h1></body></html>"


@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
