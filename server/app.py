from flask import Flask 
app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index ():
    return "<h1>Welcome to flatiron cars</h2>"

@app.route('/<models>')
def check_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'
    