from flask import Flask
app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route("/")
def home():
    """
    Default route that introduces the company.
    """
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def get_model(model):
    """
    Checks whether a requested model exists in the fleet.
    Returns an appropriate message based on the result.
    """
    if model.lower() in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)