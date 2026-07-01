from flask import Flask

# List of car models currently in the Flatiron Cars fleet.
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)


@app.route('/')
def index():
    '''Default route: introduces the company.'''
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model(model):
    '''Model-specific route: reports whether the requested model is in the fleet.'''
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)