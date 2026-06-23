from flask import Flask

app = Flask(__name__)

# Existing models in the fleet
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
    Returns appropriate message based on result.
    """

    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"


# Only runs locally
if __name__ == "__main__":
    app.run(debug=True)