FROM python:3.10-slim

# Set the working directory
WORKDIR /my_pro

# Install dependencies for psycopg2 (PostgreSQL development libraries)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev && \
    pip install --upgrade pip

# Copy requirements file and install dependencies
COPY my_pro/requirements.txt /my_pro/
RUN pip install --no-cache-dir -r /my_pro/requirements.txt

# Copy the rest of the application code
COPY . /my_pro/

# Expose port 8000 to access the app
EXPOSE 8000

# Start the Django development server
CMD ["python", "my_pro/manage.py", "runserver", "0.0.0.0:8000"]

