# ToDo Project
This is a test project.

# Time Track

- 12 May : 2h
- 13 May : 4h
- 14 May : 8h
- 15 May : 7h

# Run

## Local

- install requirements:

        pip install -r requirements.txt
- make migrations and migrate (just for first time command to init db):

        python manage.py makemigrations
        python manage.py migrate

- run the project:

        python manage.py runserver

Now checkout `localhost:8000`.

## Dockerize
First you need to build the docker images:

    docker-compose build

Run:

    docker-compose up -d

Checkout at `localhost:8585`.

Note: Make sure about migrations:

    docker-compose exec app python manage.py makemigrations
    docker-compose exec app python manage.py migrate
