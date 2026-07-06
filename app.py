from flask import Flask 

app = Flask(__name__)

existing_models = ["Model S", "Model 3", "Model X", "Model Y"]

@app.route('/')
def index():
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def model(model):
    if model in existing_models:
        return f'Flatiron{model} is in your fleet!'
    else:
        return f"No models called {model} exists in our catalog."
    

if __name__ == "__main__":
    app.run(debug=True)