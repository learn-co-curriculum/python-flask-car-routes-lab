from flask import Flask

app = Flask(__name__)

models = ["Beedle", "Crossroads", "M2", "Panique"]


@app.route("/")
def index():
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def model(model):
    if model in models:
        return f"Flatiron {model} is in our fleet!"
    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
