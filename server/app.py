from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# List of existing car models in the fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route


@app.route("/")
def home():
    """
    Default landing page route.
    Returns a welcome message for Flatiron Cars.
    """
    return "Welcome to Flatiron Cars"

# Dynamic route for specific car models


@app.route("/<model>")
def car_model(model):
    """
    Route that checks if a given model exists in the fleet.
    Case-insensitive comparison so users can type any capitalization.
    """
    for m in existing_models:
        if model.lower() == m.lower():
            return f"Flatiron {m} is in our fleet!"
    return f"No models called {model} exists in our catalog"


# Run the app locally for testing
if __name__ == "__main__":
    app.run(debug=True)
