from flask import Flask

app = Flask(__name__)


existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route("/")
def index():
    """
    Default route.
    Returns a welcome message for the Flatiron Cars company.
    """
    return "Welcome to Flatiron Cars"

@app.route("/<model>")
def model_lookup(model):
    """
    Route for looking up a specific car model.
    If the model exists in the existing_models list (case-insensitive), 
    returns a success message.
    Otherwise, returns a failure message.
    """
    if model.lower() in (m.lower() for m in existing_models):
        return f"Flatiron {model} is in our fleet!"
    return f"No models called {model} exists in our catalog"

if __name__ == "__main__":
   
    app.run(debug=True, port=5555)