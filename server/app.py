
from flask import Flask

# Initialize the Flask application.
app = Flask(__name__)

# Existing car models used by the application.
existing_models = ["Crossroads"]


# Default route.
@app.route("/")
def index():
    return "Welcome to Flatiron Cars"


# Route for checking a specific car model.
@app.route("/<model>")
def model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"
