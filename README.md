
# Run the container
```bash
docker compose up
```

# Run migrations inside the container
```bash
docker compose -f docker-compose.yml exec app bash
alembic revision --autogenerate
alembic upgrade head
```

# Access to app:
- Flask App Documentation at http://localhost:5000/apidocs/ 
    Test endpoints using token: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
- Database viewer run at http://localhost:8080/ (user: postgres, password: postgres)


# Run without docker

## Install dependencies using poetry

```bash
# Install poetry ...
poetry shell # start virtual enviroment
poetry install # install dependencies
```
## Run app
```bash
flask --app src.app:app run --reload --debug
```


# Aditionals commands for development (optional)

## Check styles

```bash
python manage.py check styles
# or
pylint src
```

## Check types
```bash
python manage.py check types
# or
mypy .
```

## Run tests
```bash
python manage.py run tests
# or
pytest
```

## Format code

```bash
python manage.py run formatter
# or
black src
```

##  Run pre-commit settings

```bash
python manage.py run precommit
# or
pre-commit install
pre-commit run --all-files
```
