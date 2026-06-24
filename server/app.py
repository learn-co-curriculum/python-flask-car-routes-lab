from flask import Flask, jsonify  # type: ignore[import]
app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    return 'WElcome to Flatiron Cars'


@app.route('/<model>')
def get_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'



if __name__ == '__main__':
    app.run(debug=True)