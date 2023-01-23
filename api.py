from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def form():
    return "<h1>test.html</h1>"

@app.route("/2", methods=["POST"])
def submit():
    name = request.form.get("name")
    return "Hello, " + name

if __name__ == "__main__":
    app.run(debug=True)


