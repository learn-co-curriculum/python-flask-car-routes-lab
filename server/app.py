# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class (this represents our web app)
app = Flask(__name__)

# A list of existing car models in our fleet
existing_models = ['Beetle', 'Crossroads','M2', 'Panique']

# Define the default route (home page)
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"    # Returns a welcome message when visiting the root URL

# Define a dynamic route that accepts a car model as part of the URL
@app.route('/<model>')
def car_model(model):
# Check if the given model is in our list of available models
    if model in existing_models:
    # Return a message confirming the model is in the fleet
        return f"Flatiron {model} is in our fleet!"
    else:
    # Return a message stating the model doesn't exist in the catalog
        return f"No models called {model} exists in our catalog"

# Run the app only if this file is executed directly (not imported)
if __name__ == '__main__':
    app.run(debug=True)
