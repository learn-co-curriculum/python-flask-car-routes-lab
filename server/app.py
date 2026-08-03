from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Default route introducing the car company
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'


# Route for checking whether a specific car model is in our fleet
@app.route('/<model>')
def model_route(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'