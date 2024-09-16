2. Docker
=========


1. Build a Docker image to run the app locally
----------------------------------------------

    Download and install Docker `<https://docs.docker.com/get-started/get-docker/>`_

    Change to the project directory cd /path/to/Python-OC-Lettings-FR

    Make sure that the .venv file has been previously created (see Developement packages)

    Build image docker build -t <image-name> . with the desired image name

    Use docker run --rm -p 8000:8000 <image-name> command, replacing image-name with the one built before

    You can access the app in any web browser at http://127.0.0.1:8000/


2. Pull an existing image from DockerHub to run the app locally
---------------------------------------------------------------
    Download and install Docker

    Go to the Docker repository: `<https://hub.docker.com/r/fcr77/my-app/tags>`_

    Copy the tag you would like to use (preferably the most recent)

    Use docker run --rm -p 8000:8000 fcr77/my-app/tags 

    You can access the app in any web browser at http://127.0.0.1:8000/