from flask import Flask
app = Flask(__name__)

#the predefined models for lookup
models = ["SUV", "Sedan", "Truck", "Coupe", "Convertible"]

@app.route('/')
def home():
    return"Welcome to Flatiron Cars"

@app.route('/<model>')
def check_model(model):
    if model in models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"Sorry, we do not have {model} in our fleet."

if __name__ == '__main__':
    app.run(debug=True)