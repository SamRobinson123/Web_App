FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Add application code
ADD Root .

# Copy requirements file
COPY Root .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY .. .

# Expose port 8080
EXPOSE 8080

# Set environment variable for Flask app
ENV FLASK_APP=WebApp.py

# Start Gunicorn server on port 8080
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "WebApp:app"]
