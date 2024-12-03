FROM python:3.10-slim

# Disable .pyc creation and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /my_pro

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev apache2 apache2-dev libapache2-mod-wsgi-py3

# Upgrade pip and install Python dependencies
COPY my_pro/requirements.txt /my_pro/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /my_pro/requirements.txt

# Copy the entire project directory into the container
COPY my_pro /my_pro/

# Configure Apache to use mod_wsgi for the Django app
RUN echo '
<VirtualHost *:80>
    ServerName localhost

    DocumentRoot /my_pro

    <Directory /my_pro>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess my_pro python-home=/my_pro/env python-path=/my_pro
    WSGIProcessGroup my_pro
    WSGIScriptAlias / /my_pro/my_pro/wsgi.py
</VirtualHost>' > /etc/apache2/sites-available/000-default.conf

# Expose HTTP port
EXPOSE 80

# Start Apache in foreground
CMD ["apache2ctl", "-D", "FOREGROUND"]

