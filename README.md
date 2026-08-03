# Lab: Introduction to Flask - Car Routes

## Overview

This project is a Flask application that provides routes for a car company database. The application demonstrates how to create Flask routes, handle URL parameters, and return different responses based on whether a car model exists in the company's fleet.

## Features

The application provides two main routes:

* `/` — Default route introducing the car company
* `/<model>` — Model-specific route for checking whether a car model is in the fleet

## Technologies Used

* Python 3.8.13
* Flask 2.2.2
* pytest
* Pipenv
* Git and GitHub

## Application Routes

### 1. Home Route

**Endpoint:**

```text
GET /
```

**Response:**

```text
Welcome to Flatiron Cars
```

This route provides the welcome message for the car company.

### 2. Car Model Route

**Endpoint:**

```text
GET /<model>
```

The route accepts a car model from the URL and checks it against the following list of existing models:

```python
['Beedle', 'Crossroads', 'M2', 'Panique']
```

#### Existing Model

For example:

```text
/Beedle
```

returns:

```text
Flatiron Beedle is in our fleet!
```

#### Model Not in the Catalog

For example:

```text
/realCar
```

returns:

```text
No models called realCar exists in our catalog
```

## Project Structure

```text
python-flask-car-routes-lab/
├── server/
│   ├── app.py
│   └── testing/
│       ├── app_test.py
│       └── conftest.py
├── screenshots/
│   └── flask-home.png
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
```

## Setup and Installation

Clone the repository and navigate into the project directory.

Install the project dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

Verify Flask:

```bash
flask --version
```

## Running the Application

Set the Flask application:

```bash
export FLASK_APP=server/app.py
```

Start the Flask development server:

```bash
flask run
```

The application can then be accessed at:

```text
http://127.0.0.1:5000/
```

## Testing

The application was tested using the provided pytest test suite.

Run:

```bash
pytest -v
```

All five tests passed successfully:

```text
5 passed
```

The tests verify:

* The `/` route exists.
* The `/` route returns the correct welcome message.
* The `/<model>` route exists.
* An existing model returns the correct fleet message.
* A model that does not exist returns the correct catalog message.

## Completed Application Screenshot

The screenshot below shows the completed Flask application's home route:

![Flask Car Routes Home](screenshots/flask-home.png)

## Best Practices Implemented

* Added comments to explain the purpose and logic of the Flask routes.
* Used a feature branch for development.
* Tested the application using pytest.
* Manually tested the Flask routes using a web browser.
* Documented the completed functionality in this README.
* Added a screenshot of the completed application.
* Kept the application code clean and free of unnecessary commented-out code.

## Git Workflow

The project was developed using a feature branch and will be committed and pushed to GitHub before being merged into the `main` branch.

## Grading Criteria

The application satisfies the required functionality:

* `/` route exists and returns correctly.
* `/<model>` route exists and returns correctly.
* All provided tests pass successfully.

## Submission

After the final changes are committed and pushed to the `main` branch, the repository can be submitted through Canvas using CodeGrade.
