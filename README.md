# Django Template

A generator for pre-configured Django projects, distributed as a Docker image
via **GitHub Packages (GHCR)**.

Running the image creates a complete new Django project with Tailwind CSS,
SQLite, Gunicorn and an initial app structure already set up — ready to start
developing.

## What the template comes with

- Django project (`core`) and initial app (`app`) already created and wired up
- [django-tailwind](https://github.com/timonweb/django-tailwind) installed and configured
  (Tailwind v4 standalone binary, no Node.js required)
- A "Premium Minimal" design system: design tokens, light/dark themes and
  ready-made components (buttons, cards, badges, alerts, forms, tables) — see
  [`django-template/docs/visual-identity.md`](django-template/docs/visual-identity.md)
- SQLite database at `data/db.sqlite3`
- Cache configured to use the database (`DatabaseCache`)
- Base connector (`BaseDBConnector`, via SQLAlchemy) for external databases
- `.env` with an automatically generated `DJANGO_SECRET_KEY`
- `Dockerfile` and `docker-compose.yml` ready to build/deploy the generated
  project (Gunicorn + Nginx + volumes for SQLite and static files)
- Git repository already initialized (`git init`) in the generated project

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- Read access to the image on GHCR (if the package is private, a token with
  the `read:packages` scope)

> In the commands below, replace `<owner>/<repo>` with this repository's
> owner and name on GitHub (lowercase).

## Usage

### 1. (If the package is private) Authenticate Docker with GHCR

Using the [GitHub CLI](https://cli.github.com/):

```bash
gh auth token | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
```

### 2. Pull the image

```bash
docker pull ghcr.io/<owner>/<repo>:latest
```

### 3. Generate a new project

The image creates the project inside `/app/<project-name>`. Mount a volume
pointing to that same path so the generated files are available on your
machine:

```bash
docker run --rm -it \
  -v "$PWD/my_project:/app/my_project" \
  ghcr.io/<owner>/<repo>:latest my_project
```

Without the final argument, the script asks for the name interactively
(default: `main_app`) — in that case, mount the volume using the same name you
type.

When it finishes, the project will be available at `./my_project`, ready to be
opened and versioned.

### 4. Run the generated project

```bash
cd my_project
docker compose up --build      # http://localhost:8080 (port via HTTP_PORT in .env)
```

## Repository structure

```
.
├── Dockerfile              # Image that generates new projects (published to GHCR)
├── entrypoint.sh           # Interactive script that builds the Django project
├── tailwind/
│   └── styles.css          # Design system; replaces theme/static_src/src/styles.css after `tailwind init`
├── django-template/        # Files copied into every generated project
│   ├── app/                # Initial Django app (models, views, templates...)
│   ├── core/               # The project's settings.py and urls.py
│   ├── docs/               # Visual identity specification
│   ├── nginx/              # Reverse proxy for the generated project
│   ├── AGENTS.md           # Guide for AI agents working on the generated project
│   ├── Dockerfile          # Deployment image for the generated project
│   ├── docker-compose.yml  # Orchestration (web + nginx) for the generated project
│   └── .env.example
└── .github/workflows/      # Build and publish pipeline to GHCR
```

## CI/CD

The [`docker-publish.yml`](.github/workflows/docker-publish.yml) workflow
automatically builds and publishes the image to `ghcr.io/<owner>/<repo>:latest`
on every push to the `main` branch. The image name is derived from the
repository itself, so no extra configuration is needed in a fork.
