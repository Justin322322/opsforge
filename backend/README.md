# OpsForge Django Backend

Django backend for the OpsForge internal tools platform, using HTMX for progressive enhancement.

## Setup

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Frontend: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Project Structure

```
backend/
├── manage.py
├── opsforge/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── opsforge_app/       # Main Django app
│   ├── models.py       # Database models
│   ├── views.py        # HTMX views
│   ├── urls.py         # URL routing
│   └── admin.py        # Django admin configuration
├── templates/          # HTML templates
│   ├── index.html
│   └── partials/       # HTMX partial templates
├── requirements.txt
└── README.md
```

## Models

- **UserProfile**: Extended user profile with roles and status
- **AuditLog**: System audit trail
- **FeatureFlag**: Feature flags for gradual rollouts
- **QueueTask**: Queue tasks for ops console
- **Activity**: Recent activity feed

## HTMX Integration

All views return HTML partials that HTMX can swap into the DOM. Views are designed to work with HTMX attributes:

- `hx-get`: Load content via GET
- `hx-post`: Submit forms via POST
- `hx-target`: Target element for content swap
- `hx-swap`: How to swap content

## Static Files

Static files (CSS, JS, images) are served from the `assets/` directory in the parent folder. Configured in `settings.py`:

```python
STATICFILES_DIRS = [
    BASE_DIR.parent / 'assets',
]
```

## Development

- **Django Admin**: Access at `/admin/` after creating superuser
- **HTMX Partials**: All partials are served from `/partials/` URLs
- **Database**: SQLite by default (change in `settings.py` for production)

## Production Deployment

1. Set `DEBUG = False` in `settings.py`
2. Update `SECRET_KEY` with a secure value
3. Configure proper database (PostgreSQL recommended)
4. Set up static file serving (WhiteNoise or CDN)
5. Configure `ALLOWED_HOSTS`
6. Set up proper security headers

