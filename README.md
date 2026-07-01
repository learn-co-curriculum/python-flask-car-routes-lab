# Flatiron Cars API

A simple Flask application that demonstrates basic routing by introducing a car company and allowing users to check whether a specific car model is available in the company's fleet.

## Features

* Home route that welcomes users to the application.
* Dynamic route that accepts a car model as a URL parameter.
* Checks whether the requested model exists in the company's catalog.
* Returns an appropriate message depending on whether the model is available.

## Project Structure

```text
python-flask-car-routes-lab/
├── server/
│   └── app.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── pytest.ini
```

## Installation

1. Clone the repository.

```bash
git clone git@github.com:wanja-juma/python-flask-car-routes-lab.git
```

2. Navigate to the project directory.

```bash
cd python-flask-car-routes-lab
```

3. Install the project dependencies.

```bash
pipenv install
```

4. Activate the virtual environment.

```bash
pipenv shell
```

## Running the Application

Start the Flask development server:

```bash
flask --app server.app run
```

The application will be available at:

```text
http://127.0.0.1:5000
```

## Available Routes

### Home Route

**Endpoint**

```text
/
```

**Method**

```text
GET
```

**Response**

```text
Welcome to Flatiron Cars
```

---

### Model Route

**Endpoint**

```text
/<model>
```

**Method**

```text
GET
```

If the requested model exists in the fleet:

```text
Flatiron Corolla is in our fleet!
```

If the requested model does not exist:

```text
No models called Ferrari exists in our catalog
```

## Example Requests

Visit the following URLs in your browser:

```text
http://127.0.0.1:5000/
```

```text
http://127.0.0.1:5000/Corolla
```

```text
http://127.0.0.1:5000/Ferrari
```

## Technologies Used

* Python 3
* Flask
* Pipenv

## Display Image

Screenshot 2026-07-02 002605.png

Screenshot 2026-07-02 002633.png

## Author

Ruth Juma
