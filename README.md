## About
### Overview 
This project aims to participate in the selection process of the company Code7

### Description
The design goal is to have a backend with tools to help deliver an API.

## Requirements
- Python 3.8.x installed.
- Pip3 20.x installed.
- Mongo 4.x installed

---

## Configure Mongo Instace
An instance of MongoDB will be required. Recommended to be installed via Docker on the same machine, following the example commands:
- Donwload the image and rename it:
```bash
$ docker container run --publish 27017:27017 -d --name mongodb mongo:latest
```

## Installation
- Clone this repository:
```bash
$ git clone https://github.com/MartinsBruno/code7
```
- Use the main directory:
```bash
$ cd code7/
```
- Install all requirements to this project
```bash
$ pip install -r requirements.txt
```
- Export the flask variable to use the main app.py file of the project
```bash
$ export FLASK_APP=news/app.py
```
- Run the application! (Specify the door if necessary. The default will be :5000)
```bash
$ flask run --port 8000
```
- Access the application in localhost:PORT

---
