FROM python:3.10-slim

# Set the working directory
WORKDIR /my_pro

# Copy the requirements file and install dependencies
COPY my_pro/requirements.txt /my_pro/
RUN pip install --no-cache-dir -r /my_pro/requirements.txt

# Copy the rest of the application code
COPY . /my_pro/

# Expose port 8000 to access the app
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

