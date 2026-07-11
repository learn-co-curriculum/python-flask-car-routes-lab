from flask import Flask

app = Flask(__name__)

# List of existing car models
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Default route
@app.route("/")
def home():
    return "Welcome to Flatiron Cars"


# Route for a specific model
@app.route("/<model>")
def get_model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
