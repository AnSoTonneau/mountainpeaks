# mountainpeaks

This project is a REST application for managing moutain peaks in a database :
* **REST API**: the web services are implemented using FastAPI. See _/main.py_
* **Database model**: the database model and access are performed using ormar and SQLAlchemy. See _/db.py_
* **Database access**: the data is stored in a PostGIS database. A pgAdmin is deployed for database management.
*  **Docker**: the application is built and deployed in docker containers. See _/docker-compose.yml_ file

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


## Running

For accessing REST API, open your browser at <a href="http://127.0.0.1:8000/" class="external-link" target="_blank">http://127.0.0.1:8000/</a>.
For database management, open your browser at <a href="http://127.0.0.1:5050/" class="external-link" target="_blank">http://127.0.0.1:5050/</a> and login with email "admin@app.com/admin" and password "admin"
