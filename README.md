# NPI calculator Server App

Server application par for NPI calculator build with FastAPI. A calculator that use Reverse Polish Notation (RPN) alogrithm to make calculations.
Works with the [NPI calculator client application](https://github.com/Nestuna/ayomi-npi-calculator-frontend)

## Requirement

-  Python >= 3.11
-  pipenv [https://pypi.org/project/pipenv/][https://pypi.org/project/pipenv/]
-  docker
-  docker-compose

## Installation

First you have to set environement variables in .env for database
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<your-password>
POSTGRES_DB=postgres
DATABASE_URL=postgresql://postgres:<password>@db:5432/postgres
```

Build and run the containers with docker-compose

```
docker-compose up --build
```

Your server runs at `http://0.0.0.0:8000`
