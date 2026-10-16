FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1

WORKDIR /app

RUN mkdir -p /app/data

RUN chmod -R 777 /app/data

# System dependencies. Add packages required by the project's Python
# libraries here (e.g. database drivers, PDF generation libraries).
# RUN apt-get update && \
#   apt-get install -y --no-install-recommends \
#   build-essential \
#   && rm -rf /var/lib/apt/lists/*

# Gunicorn to serve the Django application
RUN pip install --no-cache-dir gunicorn

# Dependency installation. By default, django and django-tailwind are included
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Runs the startup routine. More details in the 'entrypoint.sh' file
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Default serving command, for standalone testing.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application", "--workers", "5", "--timeout", "300"]
