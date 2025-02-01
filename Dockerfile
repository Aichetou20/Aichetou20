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
# Create log directory with proper permissions
RUN touch /app/django_errors.log && chown myuser:myuser /app/django_errors.log
USER myuser

EXPOSE 8000

# Use Django development server with verbose output
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py seed_data && python manage.py runserver 0.0.0.0:8000 --verbosity 2"]
