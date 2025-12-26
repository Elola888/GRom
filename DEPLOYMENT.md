# GRom – Railway Deployment Guide

## Required Environment Variables

Set these in Railway project settings:

```
SECRET_KEY=<your-secure-django-secret-key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.railway.app,www.yourdomain.railway.app
CSRF_TRUSTED_ORIGINS=https://yourdomain.railway.app,https://www.yourdomain.railway.app
DATABASE_URL=<auto-provided-by-railway-postgres-plugin>
```

## Railway Setup Steps

1. **Create Railway project from GitHub**
   - Link your GitHub repo
   - Select this GRom repository

2. **Add Postgres plugin**
   - In Railway dashboard, add Postgres plugin
   - DATABASE_URL will be automatically added to env vars

3. **Set environment variables**
   - Go to Variables tab
   - Add SECRET_KEY, DEBUG, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS
   - DATABASE_URL will be auto-populated

4. **Deploy**
   - Railway will detect Procfile and settings.py
   - Runs: `gunicorn GRom.wsgi:application`

5. **After deployment**
   
   Create superuser:
   ```
   railway run python manage.py createsuperuser
   ```

   Run migrations:
   ```
   railway run python manage.py migrate
   ```

## Local Testing Before Deploy

```bash
# Test locally
python manage.py test

# Collect static files
python manage.py collectstatic --noinput

# Run server
python manage.py runserver
```

## Troubleshooting

- **500 errors**: Check Railway logs (railway logs)
- **Static files not loading**: Run `railway run python manage.py collectstatic`
- **Database errors**: Ensure DATABASE_URL is set and Postgres plugin is added
- **CSRF errors**: Verify CSRF_TRUSTED_ORIGINS matches your domain
