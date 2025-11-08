# Django Backend Setup Guide

## Quick Start

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Frontend: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - HTMX Partials: http://localhost:8000/partials/

## Project Structure

```
backend/
├── manage.py                 # Django management script
├── opsforge/                 # Project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── opsforge_app/            # Main application
│   ├── models.py            # Database models
│   ├── views.py             # HTMX views
│   ├── urls.py              # App URL routing
│   └── admin.py             # Django admin config
├── templates/               # HTML templates
│   ├── index.html          # Main landing page
│   └── partials/           # HTMX partial templates
├── requirements.txt         # Python dependencies
└── README.md               # Backend documentation
```

## HTMX Integration

The backend is designed to work with HTMX. All views return HTML partials that can be swapped into the DOM:

- **GET requests**: Return HTML partials for content loading
- **POST requests**: Return HTML fragments after form submission
- **URLs**: All partials are served from `/partials/` path

## Models

### UserProfile
Extended user profile with roles and status tracking.

### AuditLog
System audit trail for tracking all administrative actions.

### FeatureFlag
Feature flags for gradual feature rollouts.

### QueueTask
Queue tasks for operations console monitoring.

### Activity
Recent activity feed for dashboard.

## Adding Sample Data

To populate the database with sample data, you can:

1. Use Django admin at `/admin/`
2. Create a management command
3. Use Django shell:
   ```bash
   python manage.py shell
   ```

## Static Files

Static files (logo.svg, etc.) are served from the `assets/` directory in the parent folder. Make sure the assets folder exists with your logo file.

## Production Deployment

For production:

1. Set `DEBUG = False` in `settings.py`
2. Generate a new `SECRET_KEY`
3. Configure a production database (PostgreSQL recommended)
4. Set up proper static file serving
5. Configure `ALLOWED_HOSTS`
6. Use environment variables for sensitive settings

## Troubleshooting

### Static files not loading
- Ensure `STATICFILES_DIRS` in `settings.py` points to the assets folder
- Run `python manage.py collectstatic` in production

### Template not found
- Check that templates are in `backend/templates/`
- Verify `TEMPLATES` setting in `settings.py`

### Database errors
- Run `python manage.py migrate` to apply migrations
- Check database settings in `settings.py`

