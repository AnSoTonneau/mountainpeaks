# mountainpeaks

This project is a REST application for managing moutain peaks in a database :
* **REST API**: the web services are implemented using FastAPI. See /main.py
* **Database model**: the database model and access are performed using ormar and SQLAlchemy. See /db.py
* **Database access**: the data is stored in a PostGIS database.
*  **Docker**: the application is built and deployed in docker containers. See /docker-compose.yml file

## Requirements

Python 3.7+

For deployment:
* <a href="https://docs.docker.com/get-docker/" class="external-link" target="_blank">Docker</a>
* <a href="https://docs.docker.com/compose/" class="external-link" target="_blank">Docker compose</a>

## Deployment

<div class="termy">

```console
$ docker-compose up -d --build
```

</div>


