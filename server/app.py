from flask import Flask

app = Flask(__name__)

# List of car models currently in the Flatiron Cars fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route - welcomes visitors to the site
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

# Route that checks whether a given model is in the fleet
@app.route('/<model>')
def car_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

if __name__ == '__main__':
    app.run(port=5555, debug=True)