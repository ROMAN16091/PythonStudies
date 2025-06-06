FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PORT=8000

CMD ["gunicorn", "mysite:wsgi:application", "--bind", "0.0.0.0:8000"]