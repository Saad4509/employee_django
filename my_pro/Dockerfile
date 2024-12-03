FROM python:3.10-slim

# Disable .pyc creation and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /my_pro

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Upgrade pip and install Python dependencies
COPY my_pro/requirements.txt /my_pro/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /my_pro/requirements.txt

# Copy the entire project directory into the container
COPY my_pro /my_pro/

# Expose the application port
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_pro.wsgi:application"]

