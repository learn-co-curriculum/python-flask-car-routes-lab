from flask import Flask

app = Flask(__name__)

# Models currently in the Flatiron Cars fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    # Default route - welcomes visitors to the site
    return "Welcome to Flatiron Cars"


@app.route('/<model>')
def get_model(model):
    # Checks if the requested model exists in our fleet
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == '__main__':
    app.run(port=5555, debug=True)