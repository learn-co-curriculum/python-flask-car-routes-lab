"""
Flatiron Cars Flask Application

This application provides routes for querying car model information.
It serves as a simple API for checking if car models exist in the Flatiron Cars fleet.
"""

from flask import Flask

# Initialize Flask application instance
app = Flask(__name__)

# Available car models in the Flatiron Cars fleet
# This array contains all models currently available in the catalog
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    """
    Default route handler for the root path.
    
    Returns:
        str: A welcome message introducing Flatiron Cars to the user.
    
    Example:
        GET / -> "Welcome to Flatiron Cars"
    """
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model_route(model):
    """
    Route handler for checking if a specific car model exists in the fleet.
    
    This route accepts a model name as a URL parameter and checks if it exists
    in the existing_models array. Returns different messages based on whether
    the model is found or not.
    
    Args:
        model (str): The car model name extracted from the URL path.
    
    Returns:
        str: A message indicating whether the model exists in the fleet or not.
            - If model exists: "Flatiron {model} is in our fleet!"
            - If model doesn't exist: "No models called {model} exists in our catalog"
    
    Example:
        GET /Beedle -> "Flatiron Beedle is in our fleet!"
        GET /Tesla -> "No models called Tesla exists in our catalog"
    """
    # Check if the requested model exists in our fleet
    if model in existing_models:
        # Model found - return confirmation message
        return f'Flatiron {model} is in our fleet!'
    else:
        # Model not found - return error message
        return f'No models called {model} exists in our catalog'
