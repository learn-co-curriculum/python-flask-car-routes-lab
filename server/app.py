existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# List of car models currently available in the company's fleet
existing_models = [
    "Crossroads",
    "Corolla",
    "Camry",
    "Prius",
    "RAV4"
]


# Default route
# Displays a welcome message when a user visits the home page
@app.route("/")
def home():
    return "Welcome to Flatiron Cars"


# Dynamic route
# Accepts a car model from the URL and checks if it exists
@app.route("/<model>")
def get_model(model):
    # Check whether the requested model is in our fleet
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    # Return this message if the model is not found
    return f"No models called {model} exists in our catalog"


# Start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
