FROM python:3.10-slim

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /my_pro

# Install system dependencies for Apache HTTPD, mod_wsgi, and others
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    apache2 \
    apache2-dev \
    libapache2-mod-wsgi-py3 \
    curl \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /my_pro/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /my_pro/requirements.txt

# Copy the entire project directory into the container
COPY . /my_pro/

# Write the Apache configuration inline
RUN echo '<VirtualHost *:80>' > /etc/apache2/sites-available/000-default.conf && \
    echo '    ServerName localhost' >> /etc/apache2/sites-available/000-default.conf && \
    echo '    ProxyPass / http://127.0.0.1:8000/' >> /etc/apache2/sites-available/000-default.conf && \
    echo '    ProxyPassReverse / http://127.0.0.1:8000/' >> /etc/apache2/sites-available/000-default.conf && \
    echo '</VirtualHost>' >> /etc/apache2/sites-available/000-default.conf

# Expose port 80 for HTTP
EXPOSE 80

# Start Apache HTTPD and Gunicorn
CMD service apache2 start && gunicorn --bind 0.0.0.0:8000 my_pro.wsgi:application

