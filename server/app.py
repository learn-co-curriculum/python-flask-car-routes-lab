from flask import Flask

app = Flask(__name__)

# Models recognized by the catalog route.
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route("/")
def index():
    """Introduce the car company on the home page."""
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def show_model(model):
    """Report whether the requested model is part of the fleet."""
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
