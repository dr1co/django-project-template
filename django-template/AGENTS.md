# AGENTS.md

A guide document for AI Agents.

---

## Current project state

**Phase:** template/scaffold, not yet specialized. The business purpose **has
not been defined** yet (to be provided later, ask the user if needed).

This is a **generic base Django template**: layout, session-based auth,
external database connectors, and Docker infra. No business logic, no models,
no tests.

"Still a template" markers that should disappear once the project is defined:

- `.env` — `DJANGO_DEBUG_MODE="True"` and `DJANGO_ALLOWED_HOSTS="*"` (read in
  [core/settings.py:32-34](core/settings.py#L32-L34))
- [app/templates/base.html:9](app/templates/base.html#L9) — placeholder title
  ("DON'T FORGET TO CHANGE THE APPLICATION TITLE!")
- [app/templates/base.html](app/templates/base.html) — "New App" name, "N"
  symbol and "Application subtitle" placeholders (sidebar header **and** top
  bar), plus the "New App" footer; no logo or favicon yet
  (`app/static/app/assets/` is empty)
- [app/templates/home.html](app/templates/home.html) — generator landing page
  with a component reference (buttons, badges, form, table); replace it
- [app/templates/base.html](app/templates/base.html) sidebar — example
  menu items ("Menu Item 1", "Collapsible Menu", subitems A/B)
- [app/views.py](app/views.py) — all three views are demo code (`home_view`,
  `logged_in_view`, `logged_out_view`)
- [app/models.py](app/models.py) — no ORM model yet
- [app/admin.py](app/admin.py) — no model registered yet
- [app/tests/](app/tests/) — no test yet
- `theme/templates/base.html` — django-tailwind default, unused

**Git:** branch `master`, no commits yet; all content untracked.

---

## Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2.15 (docstrings reference the 6.0 docs) |
| Internal DB | SQLite at `data/db.sqlite3` |
| External DBs | SQLAlchemy 2.0.50 (raw SQL) — install the dialect's driver per project |
| Frontend | Django Templates + Tailwind CSS v4 (`django-tailwind`, standalone binary — no Node.js) |
| Design system | "Premium Minimal" — [docs/visual-identity.md](docs/visual-identity.md), implemented in `theme/static_src/src/styles.css` |
| JS | Vanilla — no framework, no build step |
| Server | Gunicorn (5 workers, 300s timeout) |
| Proxy | Nginx (public port `HTTP_PORT`, default **8080** → 80 → web:8000) |
| Deploy | Docker + docker-compose |
| Config | `python-dotenv`, `.env` at the root |

Python 3 (`python:3-slim`), with no extra system packages. When a library
needs one (a DB driver such as an ODBC driver, Cairo/Pango for PDFs, a locale),
add it in the commented `apt-get` block of the [Dockerfile](Dockerfile) and
record it here.

---

## Structure

```
.
├── core/                     # Django project (settings, root urls, wsgi, asgi)
├── app/                      # Main app — where almost everything happens
│   ├── views.py              # Views
│   ├── urls.py               # App routes
│   ├── models.py             # ORM models + BaseDBConnector (external DBs)
│   ├── context.py            # Context processors (NOT Django default)
│   ├── decorators.py         # View decorators (NOT Django default)
│   ├── admin.py, apps.py
│   ├── migrations/
│   ├── templates/            # base.html, logged_in.html, logged_out.html, home.html
│   ├── static/app/           # js/base.js, assets/
│   └── tests/                # unit/ (models, BaseDBConnector) and e2e/ (views)
├── theme/                    # django-tailwind app (TAILWIND_APP_NAME)
│   ├── static_src/src/styles.css   # Tailwind source = design tokens + components
│   └── static/css/dist/            # generated build (gitignored)
├── docs/visual-identity.md   # Visual identity / design system specification
├── nginx/                    # Dockerfile.nginx + nginx.conf
├── data/                     # SQLite (gitignored)
├── Dockerfile, docker-compose.yml, entrypoint.sh
├── requirements.txt, manage.py, .env / .env.example
```

A new Django app must be registered in `INSTALLED_APPS`
([core/settings.py:39-54](core/settings.py#L39-L54)) and have its urls included
in [core/urls.py](core/urls.py).

---

## Code conventions

### Python formatting

All Python follows **[PEP 8](https://peps.python.org/pep-0008/)**, and the
whole codebase passes `flake8` with its defaults. Check before finishing a task:

```bash
pip install flake8             # dev tool, not in requirements.txt
flake8 --exclude=theme,data,staticfiles .
```

- **4-space indentation**, no tabs — code, data structures and the examples
  inside docstrings alike.
- **79-character lines.** Break long strings with implicit concatenation
  inside parentheses, not backslashes:
  ```python
  "NAME": (
      "django.contrib.auth.password_validation."
      "UserAttributeSimilarityValidator"
  ),
  ```
- **Double quotes** for strings everywhere (PEP 8 only asks for consistency;
  this is the project's choice). Single quotes only to avoid escaping.
- Two blank lines around top-level functions and classes, one between
  methods. Two blank lines between conceptual blocks in `settings.py`.
- Imports in three groups separated by a blank line: standard library,
  third-party (Django included), local (`from . import ...`). Import names you
  use; scaffolding files that keep an unused Django import (e.g.
  `from django.contrib import admin` in `admin.py`) mark it `# noqa: F401`.
  Remove the marker once the import is used.
- Trailing commas in multi-line collections and calls.
- No trailing whitespace, and files end with a single newline.
- `manage.py`, `core/wsgi.py` and `core/asgi.py` are Django-generated and
  already conform; leave them as they are.

### Language

- **All comments, docstrings, log messages, and UI text are in English**,
  including function, variable, and route names (`home_view`,
  `logged_in_view`, `current_user`, `user_data`). Templates use
  `<html lang="en">`.
- `LANGUAGE_CODE = "en-us"` and `TIME_ZONE = "UTC"` keep Django's defaults. If
  real localization is needed, adjust and record it here.

### Module docstrings — an important pattern

Every file in `app/` and `core/` opens with a long, teaching-style docstring:

1. What the file does;
2. Why it exists (noting when the file is **not** Django-default — the case for
   `context.py` and `decorators.py`);
3. A link to the official Django docs;
4. Numbered, commented usage examples.

Right below it comes an invite line — `# Create your views here.`,
`# Create your decorators here.`, `# Register your models here.`.

**Keep this pattern** for new structural files. Write real code **below** the
invite line; never delete the docstring.

### Views

- Function-Based Views by default; CBVs are allowed (documented in `views.py`'s
  docstring) but unused in the template.
- `render(request, "template.html", context)`.
- Template views stay separate from API views, which hold business rules,
  queries, external API calls, etc.
- Naming: template views are `<page_url_suffix>_view` (`/dashboard` →
  `dashboard_view`, `/logged-in` → `logged_in_view`); API views are
  `<endpoint_suffix>` (e.g. `api_erp_registration`).

### URLs

- Routes live in `app/urls.py`; `core/urls.py` only does `include`.
- `name=` mirrors the view name and the path mirrors the route (convention
  stated in the file itself):
  `path("logged-in", views.logged_in_view, name="logged_in_view")`.
- No trailing slash (`"logged-in"`, not `"logged-in/"`); multi-word paths use
  hyphens.
- API paths always start with the `api` prefix and follow the scope of the
  service or rule — e.g. an ERP query lives under
  `api/erp/<specific_service>`.

### Authentication and session

The template **does not use `django.contrib.auth` for application login** —
sessions are handled manually:

- Login = write `request.session["user_data"]`; logout =
  `request.session.flush()`.
- View protection = `@auth_required`
  ([app/decorators.py:24](app/decorators.py#L24)), which redirects to `/` when
  `user_data` is absent.
- The `global_data` context processor
  ([app/context.py:33](app/context.py#L33)) injects `current_user` into **all**
  templates (not `user`, which would shadow `django.contrib.auth`'s variable).
- Templates check `{% if request.session.user_data %}` to show/hide the sidebar.

Expected `user_data` shape (documented in `context.py`):

```python
user_data = {
  "user_reg": "user's registration number",
  "name": "name",
  "email": "email",
}
```

Sessions last 14 days (`SESSION_COOKIE_AGE = 1209600`) and survive browser
close.

### Database

Two paths, documented in [app/models.py](app/models.py):

1. **Django ORM** — local tables. Always define `class Meta: db_table =
   "tb_name"` explicitly.
2. **`BaseDBConnector`** — external/legacy databases (ERPs, data warehouses,
   third-party systems) via SQLAlchemy + raw SQL. Subclass it, build
   `self.conn_string` in `__init__`, and add specific methods that call the
   base methods.

| Method | Return on success | Return on error |
|---|---|---|
| `fetchone_read_query(query, params)` | `dict` or `None` | `None` |
| `fetchall_read_query(query, params)` | `list[dict]` (`[]` if empty) | `None` |
| `execute_write_query(query, params)` | `bool` (rowcount > 0) | `False` |

Characteristics to respect:

- **Always use `params` (bind parameters), never f-strings in the query** —
  this is the template's SQL injection protection.
- Pooled engine (`pool_size=5`, `max_overflow=0`, `pool_recycle=1800`,
  `pool_pre_ping=True`), created lazily and cached in `self._engine`.
- Credentials go through `quote_plus`.
- Errors are **swallowed**: error + traceback are `print`ed and a neutral value
  returned — no exceptions, no `logging`. If this changes, change it
  project-wide and record it here.

### Templates

- `app/templates/base.html` is the master layout; **every** screen
  `{% extends 'base.html' %}` (including `home.html`). Blocks: `title`,
  `extra_head`, `page_header`, `content`, `extra_script`.
- Application shell: a `w-64` dark sidebar appears only with an active session
  (fixed on `lg+`, off-canvas with a toggle button below `lg`); the content
  column gets `lg:pl-64` in that case. This lives in `base.html` only — screens
  don't add offsets themselves.
- Page header goes in `{% block page_header %}`: `.page-title` (+ optional
  `.page-description`) and at most one primary action. Not a hero section.
- Active menu item: `{% if request.resolver_match.url_name == 'url_name' %}`
  → `bg-white/10 text-white` + `aria-current="page"`. Update the names when
  creating real routes.
- Messages use `django.contrib.messages`, rendered as `.alert` mapped from
  `message.tags` (`success`, `error` → danger, `warning`, default → info),
  always with an icon + text (status never relies on color alone).

### Design system / CSS

The visual identity is specified in
[docs/visual-identity.md](docs/visual-identity.md) ("Premium Minimal": navy +
steel blue, cool neutrals, thin borders, no card shadows). Read it before
designing a screen and run its §20 checklist before calling a page done.

It is implemented in **`theme/static_src/src/styles.css`** (Tailwind v4,
CSS-first config — there is no `tailwind.config.js`):

1. **Runtime tokens** — `--ui-*` variables on `:root` (light) and
   `[data-theme="dark"]`. The only place raw theme colors live; rebrand here.
2. **`@theme`** — maps tokens to utilities. Use these, never raw hex or
   Tailwind's stock palette (`gray-*`, `green-*`...) in templates:

   | Purpose | Utilities |
   |---|---|
   | Surfaces | `bg-canvas` (page), `bg-surface` (cards), `bg-surface-secondary` (highlight/selected), `bg-surface-elevated` |
   | Text | `text-fg`, `text-fg-secondary`, `text-fg-muted` (metadata only — not on `surface-secondary`) |
   | Borders | `border-line`, `divide-line` |
   | Brand / interaction | `text-brand`, `bg-accent`/`text-accent` (interactive only), `text-on-accent` |
   | Sidebar | `bg-sidebar`, `text-sidebar-fg`, `text-sidebar-muted`, `border-sidebar-line` |
   | Semantic | `success`, `warning`, `danger`, `info` + `-subtle` backgrounds |
   | Fixed palette | `navy`, `steel`, `mist`, `neutral-{50…950}` (doc's scale, replaces Tailwind's) |
   | Fonts | `font-sans` (Inter, default), `font-display` (Manrope: page titles, metrics), `font-mono` (JetBrains Mono: IDs, versions, logs) |
   | Radius | `rounded-sm` 6px (badges), `rounded-md` 8px (buttons, inputs), `rounded-card` 10px (cards), `rounded-lg` 12px |
   | Shadow | none on cards; `shadow-popover` only for floating surfaces |

3. **Components** (`@layer components`) — prefer them over re-composing
   utilities:
   - Buttons: `.btn` + `.btn-primary` | `.btn-secondary` | `.btn-ghost` |
     `.btn-danger` (+ `.btn-sm`). One primary action per section.
   - Cards: `.card` (+ `.card-compact`, `.card-interactive` for clickable
     cards only).
   - `.page-title`, `.page-description`, `.section-title`.
   - Badges: `.badge` + `.badge-neutral|success|warning|danger|info`.
   - Alerts: `.alert` + `.alert-success|warning|danger|info`.
   - Forms: `.label` (always, above the field), `.input` (also `select`,
     `textarea`), `.help-text`, `.field-error`; mark invalid fields with
     `aria-invalid="true"`.
   - Tables: `.table` (horizontal dividers only); wrap in `overflow-x-auto`.
   - Loaders: `.loader`, `.loader-white`, `.loader-spinner`.
4. **Base** — global `:focus-visible` ring and `prefers-reduced-motion`
   handling. Don't remove focus outlines.

Rules:

- **Dark mode**: `data-theme` on `<html>`, set before paint by the inline
  script in `base.html` (saved choice → system preference) and toggled by
  `#theme-toggle-button`. Tokens flip automatically; only use the `dark:`
  variant for what tokens can't express.
- **Contrast**: pairs in `styles.css` were checked for WCAG AA. Muted text
  (`#6B7279`) and success text (`#24734F`) are slightly darker than the
  identity document to pass. When adding a color, check its real
  foreground/background pairs.
- To add a token: add the `--ui-*` variable to **both** `:root` and
  `[data-theme="dark"]`, then map it in `@theme inline`.
- Icons: **inline Heroicons outline SVG** (`stroke-width="1.5"`,
  `stroke="currentColor"`, `aria-hidden="true"`), `size-4`/`size-5`/`size-6`
  (16/20/24px). Icon-only buttons need an `aria-label`.
- Motion: color/opacity transitions, 150ms default (200ms for layout). No
  scaling or continuous animation.
- Tailwind scans via `@source "../../../**/*.{html,py,js}"`, so classes can
  also live in `.py` and `.js` files. Run `python manage.py tailwind start`
  while editing templates.

### JavaScript

- Vanilla, no framework, no bundler. Global file:
  [app/static/app/js/base.js](app/static/app/js/base.js).
- Page-specific logic goes in a file named after its template (`home.html` →
  `home.js`), loaded through the `{% block extra_script %}` block.
- Wrap everything in `document.addEventListener("DOMContentLoaded", () => {})`.
- **Always check an element exists before using it** (`if (btn && list)`) — the
  script loads on every page.
- Interactive elements get an `id` with a `-button` suffix (`logout-button`,
  `menu-dropdown-button`, `theme-toggle-button`, `sidebar-toggle-button`).
- Select state through ARIA/data attributes (`aria-expanded`,
  `aria-current`, `[data-alert]`), never through styling classes — those
  change with the design.
- Message alerts (`[data-alert]`) auto-dismiss after 5s.

### Tests

- **TDD is the default workflow**: write the failing test first, then the
  code to make it pass. Exceptions (no test-first needed): pure
  style/template/copy changes, config/wiring changes (`settings.py`,
  `urls.py`), and refactors with no behavior change under existing green
  tests.
- Django's native stack only: `django.test.TestCase` + `python manage.py
  test`. No pytest, no `factory_boy`, no fixture files — test data is created
  inline (`Model.objects.create(...)`, `setUp()` for shared setup). Mocking
  is stdlib `unittest.mock` only.
- Layout — `app/tests/` package, split by test type:
  ```
  app/tests/
  ├── unit/   # models, BaseDBConnector (external calls mocked, never live)
  └── e2e/    # views
  ```
- Test class/method names are in English like the rest of the code
  (`EmployeeModelTest.test_create_employee`).
- Minimum coverage per artifact:
  - Model → a unit test creating an instance and checking its fields.
  - Template view → an e2e test asserting status code (200, or redirect if
    `@auth_required` and no session).
  - API view → an e2e test for the success path **and** the swallowed-error
    path (see [Database](#database) — errors return `None`/`False`, not
    exceptions).
- e2e tests needing a logged-in session use the shared `login_as_user()`
  helper (`SessionTestCase` in `app/tests/e2e/__init__.py`) instead of setting
  `session["user_data"]` by hand in every test.

---

## Commands

### Docker (standard flow)

```bash
docker compose up --build      # brings up web + nginx → http://localhost:8080
docker compose down
docker compose logs -f web
```

[entrypoint.sh](entrypoint.sh) runs automatically:
`migrate` → `createcachetable` → `tailwind build` → `collectstatic` → gunicorn.

### Local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createcachetable          # cache is DatabaseCache (cache_table table)
python manage.py tailwind start            # Tailwind watcher, in another terminal
python manage.py runserver
python manage.py test                      # tests
python manage.py makemigrations app
```

⚠️ `STATICFILES_STORAGE = ManifestStaticFilesStorage` requires `collectstatic`
before serving static files with `DEBUG = False`.

---

## Environment

`.env` at the root (gitignored), templated by `.env.example`:

```
DJANGO_SECRET_KEY=<string>
DJANGO_DEBUG_MODE=<False|True>
DJANGO_ALLOWED_HOSTS="*"        # comma-separated
HTTP_PORT=8080                  # host port for nginx (docker-compose)
```

 External database credentials, when they exist, go
here and are read with `os.getenv` — **never hardcoded**. Update `.env.example`
alongside it, without real values.

---

## Before going to production

- [ ] `DJANGO_DEBUG_MODE="False"` in the server's `.env`
- [ ] `DJANGO_ALLOWED_HOSTS` with real hosts, no `"*"`
- [ ] Comment out `path("admin/", ...)` in
      [core/urls.py:26](core/urls.py#L26) if admin isn't used
- [ ] Real `SECRET_KEY` in the server's `.env`
- [ ] Title, name, symbol, subtitle, footer, logo, and favicon in `base.html`
      set; `home.html` replaced
- [ ] Accent color / tokens adjusted in `theme/static_src/src/styles.css`, if
      the app has its own identity (see visual identity §18)
- [ ] Real menu items and correct `url_name`s in the sidebar
- [ ] Demo views/templates (`logged_in`, `logged_out`) removed
- [ ] Evaluate migrating off SQLite if there's write concurrency

> **KEEP THIS FILE UP TO DATE.** Update it in the same task whenever a
> structural change lands: new app, new dependency, relevant new route,
> database/infra change, convention change, or when the project's purpose is
> defined. An outdated AGENTS.md is worse than none. Check "Current project
> state" before assuming anything.
