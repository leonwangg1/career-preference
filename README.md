# LEA Career Preference Tool

A simple web-based tool for collecting Career Preference information from LEA staff.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisties

The project is built with React + TypeScript + Vite for the frontend and Python + Flask for the backend and SQLite for the database. The frontend and backend can be deployed to a Docker container.

Packages used:

- `react-router-dom` - For page routes
- `Tailwind CSS + daisyUI` - CSS framework

## Backend using Python Flask

This is a Flask-based API for managing survey questions. It uses SQLite as its database.

### Project Structure

- `app.py`: The main application file where the API endpoints are defined.
- `requirements.txt`: Contains the Python dependencies that your project needs.
- `Dockerfile`: Used to containerize the application.

### API Endpoints

- `GET /mission_capabilities`: Retrieves all mission capabilities.
- `GET /mission_capabilities/question/<int:id>`: Retrieves the mission capability with the given ID.
- `GET /fitment_questions`: Retrieves all questions where 'FitmentQuestion' is 'Yes'.
- `GET /questions/parent/<int:parent_id>`: Retrieves a parent question.
- `GET /questions/parent_id/<string:parent_text>`: Retrieves a prent question's `ParentID`
- `GET /questions/children/<int:parent_id>`: Retrieves all subquestion fom a parent question.

### Local Development

```sh
cd python-flask-api
```

1. Start in venv:

```sh
python -m venv && source venv/bin/activate
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

3. Run the application:

```sh
python app.py
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

### Local Development

```sh
cd ../career-preference
npm install
npm run dev
```
