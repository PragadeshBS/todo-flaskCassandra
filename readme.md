# Flask and Cassandra Todo App

This is a simple todo application built with Flask and Cassandra as the database. The application allows users to create, read, update, and delete tasks.

## Getting Started

To get started with this project, clone the repository to your local machine:

```
$ git clone https://github.com/PragadeshBS/todo-flaskCassandra
```

### Prerequisites

Before you can run the application, you will need to have the following installed on your machine:

- Python 3.x
- Cassandra

### Installing

To install the required dependencies, navigate to the project directory and run the following command:

```
$ pip install -r requirements.txt
```

### Running the Application

To start the application, run the following command:

```
$ python app.py
```

Once the application is running, you can access it by visiting http://localhost:5000 in your web browser.

## Usage

The application provides a simple interface for managing tasks. You can add a new task by clicking on the "Add Task" button and entering a title and description for the task. You can edit or delete a task by clicking on the corresponding icons next to the task in the list.

## Architecture

The application is built using the Flask web framework and Cassandra as the database. The Flask web server runs as a single process and handles all incoming requests. The Cassandra database is used to store the tasks and their associated metadata.

## License

Do whatever you want with this XD
