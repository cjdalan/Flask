## Installation

Start docker

To build the docker image:
```
docker build -t test:1.0 --no-cache . 
```

Change directory to test

To run the docker image:
```
docker run -it -p 80:80 -v $(pwd)/dev:/data test:1.0
```

Application will run on: http://localhost/

## Features

* 

## Structure

```
	/dev
		/core			Place important files here
		/templates		Place HTML files
		app.py
```

## Dependencies

* Flask	(Web Framework)			http://flask.pocoo.org/
* Flask WTF	(Form Helper)		https://flask-wtf.readthedocs.io/en/stable/
* Peewee (Database Library)		http://docs.peewee-orm.com/en/latest/

