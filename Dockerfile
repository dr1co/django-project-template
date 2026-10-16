FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
  curl \
  git \
  && rm -rf /var/lib/apt/lists/*

# The "cookiecutter" extra is required by `tailwind init`.
RUN pip install --no-cache-dir django sqlalchemy "django-tailwind[cookiecutter]" python-dotenv

COPY . /app/generator

# Projects are generated here. Mount the host directory that should receive
# them: docker run -v "$PWD:/workspace" ...
WORKDIR /workspace

RUN chmod +x /app/generator/entrypoint.sh

ENTRYPOINT ["/app/generator/entrypoint.sh"]
