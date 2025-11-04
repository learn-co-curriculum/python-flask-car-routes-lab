from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Our "database": in-memory list of car models that the company offers

existing_models = ['Beedle', 'Crossroads', 'H2', 'Panique']

@app.route("/")
def index():
    """
    Default route.
    Returns a short welcome message shown on the home page.
    """
    return "Welcome to Flatiron Cars"

@app.route("/<model>")
def model_lookup(model):
    """
    Dynamic route that accepts a car model name from the URL.

    - If the model exists in `existing_models`, we confirm it's available.
    - If it doesn't exist, we return a clear failure message.
    """
    if model in existing_models:
        # Success message when the model is part of the fleet
        return f"Flatiron {model} is in our fleet!"
    else:
        # Failure message when the model is unknown
        # (wording chosen to be short and explicit)
        return f"No models called {model} exists in our catalog"
