# Django Portfolio

A Persian, RTL-first personal portfolio built with Django. The project includes editable projects and experience, working authentication, a contact inbox, and a responsive dark interface.

## Requirements

- Python 3.12+
- pip

## Run locally

```bash
git clone https://github.com/aghorbani84/django-portfolio.git
cd django-portfolio
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and use /admin/ to manage portfolio content.

## Configuration

Environment variables:

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Set a unique secret key in production |
| `DJANGO_DEBUG` | Debug mode; defaults to false |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated allowed hostnames |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins including scheme |
| `DB_ENGINE` | Optional Django database engine; defaults to SQLite |
| `DB_NAME` | Database name/path |

## Content management

Create projects and experience records in Django admin. Contact submissions are stored in the admin inbox. No sample employment history or project claims are prefilled.

## Checks

```bash
python manage.py check
python manage.py test
```

## License

GPL-3.0. See [LICENSE](LICENSE).
