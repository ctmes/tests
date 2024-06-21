# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 4443 to allow access to the HTTPS server
EXPOSE 4443

# Run the https_server.py script when the container launches
CMD ["python", "https_server.py"]
