from flask import Flask


app = Flask(__name__)
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

@app.route('/<model>')
def check_models(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!."
    else:
        return f"Flatiron {model} is not in our catalog."

if __name__ == '__main__':
    app.run(debug=True)