from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Existing car models in the fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route


@app.route("/")
def home():
    """
    Default route returning welcome message for Flatiron Cars.
    """
    return "Welcome to Flatiron Cars"

# Dynamic model route


@app.route("/<model>")
def car_model(model):
    """
    Route that checks if a given model exists in the fleet.
    - If it exists, returns confirmation message.
    - If it does not exist, returns 'not found' message.
    """
    # Normalize input for case-insensitive comparison
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
