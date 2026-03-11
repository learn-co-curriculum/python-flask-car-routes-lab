# Python Flask Car Routes Lab

A simple Flask-based web application built to handle dynamic car model queries. This project was developed as part of the Flatiron School curriculum to demonstrate the fundamentals of routing and the request-response cycle.

---

## Installation

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/python-flask-car-routes-lab.git
cd python-flask-car-routes-lab
```

Install dependencies

```
pipenv install
```

Activate environment

```
pipenv shell
```

---

## Usage

Start the server:

```
python server/app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Routes

### `/`

Returns a welcome message.

```
Welcome to Flatiron Cars
```

---

### `/<model>`

Checks whether a model exists.

Example:

```
/M2
```

Response:

```
Flatiron M2 is in our fleet!
```

If not found:

```
No models called Toyota exists in our catalog
```
