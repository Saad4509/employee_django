FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /my_pro

COPY requirements.txt /my_pro/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /my_pro/

EXPOSE 8000

CMD ["gunicorn","--bind","0.0.0.0:8000","my_pro.wsgi:application"]
