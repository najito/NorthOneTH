## Takehome for NorthOne

# Objective:
```
Build a To Do List-type web application or API that meets the challenge requirements
```
I decided to make a backend API service with Python and flask.

This app uses flask and the requests python library and writes into a sqlite database

# Installation


```
brew install python3 (this will isntall pip as a dependency)
brew install sqlite

Python module requirements:
* requests
* flask
* sqlite

pip3 install -r requirements.txt

You will need to use sudo if your python3 install base is in /usr/*
```

# Database Schema
```
TABLE "items" (
    "title" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    "duedate" DATE NOT NULL,
    PRIMARY KEY("title")
);
```

# Running the App

We're using a database file locally right now but this can be changed in the future

Start the app:
```
FLASK_APP=main.py flask run
```
runs the application at 
```
127.0.0.1/5000
```

Used Postman and curl requests to test API endpoints

example curl
```
curl -X GET http://127.0.0.1:5000/item/all
```

# Methods Available

Add an item (POST)

```
endpoint: /item/new

body {
    title: string,
    description: string,
    date: string
}

returns full item with status = "Not Started"
```

Get all items (GET)

```
endpoint: /item/all

returns all tasks as an array
```

Get current item status (GET)

```
endpoint: /item/status

params = title : string

returns item
```

Update Status of item (PUT)

```
endpoint: /item/update

body: {
    title: string,
    status: ["not started", "In progress", "Completed"]
}

returns title and status as confirmation
```

Delete an item (DELETE)

```
endpoint: /item/remove

body: {
    title: string
}

return title as confirmation
```

Find by Status (GET)

```
endpoint: /item/findstatus

params = status: ["not started", "In progress", "Completed"]

returns all items with status indicated
```