#Import flask
from flask import Flask

#use Flask constructor to determine where the application is by using __name__ for app.py
app = Flask(__name__)

#sample models data
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

#define route rule for base url
@app.route('/')
def index_fn():
    return "Welcome to Flatiron Cars"

#define variable route for /<model> route => should be a string parameter
@app.route('/<string:model>')
def model_fn(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

# method to set up auto-run with 'python app.py'
if __name__ == '__main__':
    app.run(port=5555, debug=True)






