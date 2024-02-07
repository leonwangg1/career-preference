# Step 1: Build the application
# Use a Node.js base image to build the application
FROM node:16 AS build

# Set the working directory in the Docker image filesystem.
WORKDIR /app

# Copy the file containing all the dependencies to the Docker image.
COPY package.json package-lock.json ./

# Install dependencies in the Docker image.
RUN npm install

# Copy the rest of the code to the Docker image.
COPY . .

# Build the application for production.
RUN npm run build

# Step 2: Serve the application
# Use Nginx to serve the static files
FROM nginx:stable-alpine

# Copy the built app to the Nginx directory
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx configuration (if you have one)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port Nginx is listening on
EXPOSE 80

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]
