#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# List of existing car models
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
    """Default route that welcomes users to the Flatiron Cars application."""
    return 'Welcome to Flatiron Cars'

@app.route('/<model>')
def model(model):
    """
    Dynamic route that accepts a model name and checks if it exists.

    Args:
        model (str): The car model name provided in the URL
        
    Returns:
        str: A message indicating whether the model exists or not  
    """
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)