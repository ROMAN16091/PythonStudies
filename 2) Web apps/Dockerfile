FROM python:3.9-slim
WORKDIR /app
COPY reqiurements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD["gunicorn", "weather"]