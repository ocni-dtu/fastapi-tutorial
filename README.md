# FastAPI Tutorial

Tutorial for [FastAPI](https://fastapi.tiangolo.com) using [Bunnet](https://roman-right.github.io/bunnet) as an ODM
for [MongoDB](https://www.mongodb.com/)

## Tutorial
The full tutorial can be read [here](https://kongsgaard.eu/feed/fastapi-tutorial)

## Quick Start

- Clone this repo
- Make sure you have the following installed:
  - [Python 3.11](https://www.python.org/)
  - [Pipenv](https://pipenv.pypa.io/en/latest/index.html)
  - [Docker](https://docs.docker.com/get-docker/)
  - [Docker Compose](https://docs.docker.com/compose/install/)
- Install the dependencies:
  - `pipenv install --dev`
- Run tests:
  - Activate your Pipenv environment: `pipenv shell`
  - Run tests: `pytest tests/`
- Run app locally (after having activate your virtual environment):
  - `uvicorn main:app --host 0.0.0.0 --reload`
- Build Docker image:
  - `docker build --build-arg RUN_STAGE=DEV --build-arg BUILD_STAGE=DEV -t fastapi:latest .`