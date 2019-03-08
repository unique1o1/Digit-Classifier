# Digit-Classifier


## Installation

```
cd web_image-classifier 
sudo pip install -r requirements.txt
python3 app.py
```
## Docker

Another option for running this blockchain program is to use Docker.  Follow the instructions below to create a local Docker container:

1. Clone this repository
```
git clone git@github.com:unique1o1/web_image-classifier.git
cd web_image-classifier
```
2. Build the docker container

```
$ docker build Dockerfile -t web_image-classifier:latest .                 
```

3. Run the container

```
$ docker run --rm -p 80:5000 web_image-classifier
```


