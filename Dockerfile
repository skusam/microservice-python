# Basis-Image mit Python
FROM python:3.14-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Anforderungen installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projektcode kopieren
COPY app ./app

# Port für FastAPI
EXPOSE 8080

# Startbefehl für den Microservice
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
