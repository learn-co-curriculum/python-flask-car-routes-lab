from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route
@app.route("/")
def index():
    return "Welcome to Flatiron Cars"

# Route for requesting a specific car model
@app.route("/<model>")
def model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
