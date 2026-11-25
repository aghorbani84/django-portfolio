# Django Portfolio

> A Persian, RTL-first personal portfolio built with Django — with admin-managed projects and experience, user accounts, and a contact inbox.

[![Django CI](https://github.com/aghorbani84/django-portfolio/actions/workflows/django.yml/badge.svg)](https://github.com/aghorbani84/django-portfolio/actions/workflows/django.yml)
![Python](https://img.shields.io/badge/Python-3.12%20%7C%203.13-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue)](LICENSE)

## Overview

A single-page personal portfolio site written in Django with a Persian (`lang="fa"`, `dir="rtl"`) dark, responsive interface. All portfolio content — projects and work experience — is created through the Django admin, so nothing is hard-coded and no sample history is prefilled. Visitors can send messages through a contact form that lands in an admin inbox.

## Features

- **Projects** — title, summary, description, technologies, repository / live / image URLs, and a *featured* flag (featured items sort first)
- **Experience timeline** — role, company, description, start and end dates (newest first)
- **Contact form** — submissions are stored as `ContactMessage` records with a read/unread flag
- **Authentication** — sign-up (with email), login and logout using Django's auth system
- **Django admin** — list views, filters and search for projects, experience and messages
- **Environment-based configuration** — secret key, debug, allowed hosts, CSRF origins and database are read from environment variables; the app refuses to start without a secret key when debug is off
- **SQLite by default**, with any Django database engine selectable via `DB_ENGINE`

## Tech Stack

- Python 3.12+ · Django 5.2
- Django templates (Persian, RTL)
- SQLite (default)
- GitHub Actions: `manage.py check` and tests on Python 3.12 and 3.13

## Getting Started

### Prerequisites

- Python 3.12 or newer
- pip

### Run locally

```bash
git clone https://github.com/aghorbani84/django-portfolio.git
cd django-portfolio

python -m venv .venv
source .venv/bin/activate          # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

export DJANGO_DEBUG=True
export DJANGO_SECRET_KEY=local-development-key-change-me

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

On Windows PowerShell, set the variables with `$env:DJANGO_DEBUG = "True"` and `$env:DJANGO_SECRET_KEY = "local-development-key-change-me"`.

Open http://127.0.0.1:8000/ for the site and http://127.0.0.1:8000/admin/ to add projects and experience.

### Configuration

| Variable | Purpose | Default |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Secret key (required when debug is off) | — |
| `DJANGO_DEBUG` | Enable debug mode (`true` / `1` / `yes`) | `False` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hostnames | `localhost,127.0.0.1,testserver` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Comma-separated origins including scheme | empty |
| `DB_ENGINE` | Django database engine | `django.db.backends.sqlite3` |
| `DB_NAME` | Database name or path | `db.sqlite3` |

### Checks

```bash
python manage.py check
python manage.py test
```

## Project Structure

```text
django-portfolio/
├── manage.py
├── requirements.txt
├── mysite/                  # Project settings, URLs, WSGI/ASGI
├── myprofile/               # Portfolio app
│   ├── models.py            # Project, Experience, ContactMessage
│   ├── views.py             # Home (with contact form), sign-up, login
│   ├── forms.py
│   ├── admin.py
│   ├── templates/myprofile/ # base, home, login, signup
│   └── tests.py
├── site-preview/            # Static HTML preview used by the Pages workflow
└── .github/workflows/       # CI and Pages publishing
```

## License

Released under the [GNU General Public License v3.0](LICENSE).

## Author

Built by [@aghorbani84](https://github.com/aghorbani84).
