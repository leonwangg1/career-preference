# LEA Career Preference Tool

A simple web-based tool for collecting Career Preference information from LEA staff.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisties

The project is built with React + TypeScript + Vite for the frontend and Python + Flask for the backend and SQLite for the database. The frontend and backend can be deployed to a Docker container.

## Backend using Python Flask

This is a Flask-based API for managing survey questions. It uses SQLite as its database.

### Project Structure

- `app.py`: The main application file where the API endpoints are defined.
- `requirements.txt`: Contains the Python dependencies that your project needs.
- `Dockerfile`: Used to containerize the application.

### Database ERD

![image](https://github.com/leonwangg1/career-preference/assets/62505788/abad6f74-f6ea-4ff2-b381-c930ee298dc9)

### Local Development

```sh
cd python-flask-api
```

1. Start in venv:

```sh
python -m venv venv
source venv/bin/activate
```

Use `deactivate` to deactive the current virtual environment.

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

3. Run the application:

```sh
python app.py or flask run
```

### Setup and Running the Project (with Docker)

To build a Docker image of the application, run:

```sh
docker build -t flask-api .
```

To run the application in a Docker container, run:

```sh
docker run --rm -it -p 8000:8000 flask-api
```

This will start the application on port 8000.

## Frontend with Vite+React+Typescript

To allow React app (served from different port) be able to make requests to the Flask server without running into CORS issues, the `CORS(app)` part in app.py is crucial for development environments.

### Local Development

```sh
cd ../career-preference
npm install
npm run dev
```
