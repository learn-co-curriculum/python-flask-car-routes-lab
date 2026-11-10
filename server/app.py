from flask import Flask

app = Flask(__name__)

# List of cars available in our catalog
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Homepage
@app.route('/')
def home():
    return "Welcome to Flatiron Cars!"

# Check whether a car model exists
@app.route('/<model>')
def car_model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog."

if __name__ == '__main__':
    app.run(debug=True)