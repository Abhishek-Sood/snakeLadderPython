# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python project files into the container
COPY python/ .

# Expose any ports if needed (not needed for this console app)

# Command to run the application
CMD ["python", "main.py"]