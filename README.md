# mountainpeaks

This application is a simple web service for storing and retrieving moutain peaks :
* **REST API**: the web services are implemented using FastAPI. See _/main.py_
* **Database model**: the database model and access are performed using ormar and SQLAlchemy. See _/db.py_
* **Database access**: the data is stored in a PostGIS database. A pgAdmin is deployed for database management.


> **Warning**
> The database and geographical bounding box request don't use for now the specific PostGIS functions. Since I don't know PostGIS, I would need more time to use its functionnalities properly


*  **Docker**: the application is built and deployed in docker containers. See _/docker-compose.yml_ file

## Requirements

Python 3.7+

For deployment:
* <a href="https://docs.docker.com/get-docker/" class="external-link" target="_blank">Docker</a>
* <a href="https://docs.docker.com/compose/" class="external-link" target="_blank">Docker compose</a>

## Deployment

<div class="termy">

```console
$ git clone https://github.com/AnSoTonneau/mountainpeaks.git
$ cd mountainpeaks/
$ docker-compose up -d --build
```

</div>


## Running

For accessing REST API, open your browser at <a href="http://127.0.0.1:8000/" class="external-link" target="_blank">http://127.0.0.1:8000/</a>.

For testing it : http://127.0.0.1:8000/docs 

For database management, open your browser at <a href="http://127.0.0.1:5050/" class="external-link" target="_blank">http://127.0.0.1:5050/</a> and login with email admin@app.com and password _admin_
