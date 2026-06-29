from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# List of existing car models
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

# Dynamic route for car models
@app.route('/<model>')
def car_model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

# Run the Flask application
if __name__ == '__main__':
    app.run(port=5555, debug=True)