# Use the official Python image from the Docker Hub.
FROM python:3.12

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install the dependencies.
RUN pip install -r requirements.txt

# Copy the entrypoint script into the container.
COPY entrypoint.sh /entrypoint.sh

# Copy the rest of the application code into the container.
COPY . .

# Set environment variables to configure Django to use MySQL.
ENV DJANGO_SETTINGS_MODULE=messaging_system.settings
ENV PYTHONUNBUFFERED=1

# Make entrypoint script executable
RUN chmod +x /entrypoint.sh

# Expose the port the app runs on.
EXPOSE 8000

# Set the entrypoint to the entrypoint script.
ENTRYPOINT ["/entrypoint.sh"]

# Run the Django development server.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
