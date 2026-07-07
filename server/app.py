from flask import Flask

# Initialize the Flask application instance
app = Flask(__name__)

# Given array of models available in our fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# 1. Default Route ('/')
@app.route('/')
def index():
    """Returns a welcome message for the home page."""
    return 'Welcome to Flatiron Cars'

# 2. Dynamic Model Route ('/<model>')
@app.route('/<model>')
def model_lookup(model):
    """
    Takes a model name from the URL, checks if it exists in our fleet list,
    and returns the corresponding success or failure string.
    """
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

# Start the local development server if executed directly
if __name__ == '__main__':
    app.run(debug=True)
    