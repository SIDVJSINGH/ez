# Flask APP

This project is a simple Flask Application project.

I'm not so good with HTML and CSS, therefore used a simple HTML document.

This can be improved with the help of Bootstrap templates and Jinja Templating.

# File Structure:

```
Root
├───app
│    ├───templates
│    |          ├───login.html
│    |          └───dashboard.py
│    |
|    |
│    ├───__init__.py
│    │
│    ├───config.py
│    │
│    ├───models.py
│    │
│    └───routes.py
│
├───Dockerfile
├───requirements.txt
├───README.md
├───bash.sh
├───runner.sh
└───run.py
```

# Each file contains

- `app/templates/login.html` : contains the basic HTML form for Login page.
- `app/templates/dashboard.html` : contains the basic dashboard to upload and download files after login.
- `app/__init__.py` : contains the flask app object that is later used throughout the project.
- `app/config.py` : configurations for Mongodb URI and Secrets.
- `app/models.py` : contains class of User.
- `app/routes.py` : contains the application routes to forward to.
- `bash.sh` : commands to push the application on Dockerhub.
- `docker-compose.yml` : contains the linkup to the MongoDB container.
- `Dockerfile` : contains python-alpine image to run our Flask application on.
- `requirement.txt`: contains all required modules to run this Flask application on your local.
- `run.py` : the main file that runs the application from outside.
- `runner.sh` : contains bash commands to run this Flask application on your local after installation of Docker.

# This application has a Docker Image on Docker Hub

Try following command to run this on your local after installing Docker Daemon:

```
docker run -p 8000:8000 sidvjsingh/ez:1.0.0
```

This single command will pull the image from the Docker Hub and ran it in your local.

Alternatively you can also do:

```
docker pull sidvjsingh/ez:1.0.0
```

```
docker run -p 8000:8000 sidvjsingh/ez:1.0.0
```
