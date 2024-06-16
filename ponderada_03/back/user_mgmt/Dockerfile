FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 main.py create_db

CMD ["python3", "-m", "flask", "--app", "main", "run", "--host", "0.0.0.0", "--port", "83"]