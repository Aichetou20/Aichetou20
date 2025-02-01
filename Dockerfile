FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create a non-root user for security
RUN useradd -m myuser && chown -R myuser:myuser /app
USER myuser

EXPOSE 8000

# Use gunicorn for production
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py seed_data && gunicorn INPC.wsgi:application --bind 0.0.0.0:8000"]
