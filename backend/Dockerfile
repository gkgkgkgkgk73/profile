FROM python:3.12.1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# CMD ["celery", "-A", "backend", "worker", "-l", "INFO", "--autoscale=2,5"]

# CMD ["python", "manage.py" , "runserver", "0.0.0.0:8000"]

EXPOSE 8000