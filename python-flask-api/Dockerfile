# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container to /app (creates dir named app for the container)
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application to the working directory
COPY . .
ENV FLASK_APP="app.py"

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application on port 8000 when the container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]