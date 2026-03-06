# AGENTS.md - TradeAid Ghana Website

## Project Overview
This is a Django 5.0.6 web application for TradeAid Ghana (tradeaidgh.org). The project is located in the `myshop/` directory and uses:
- Django 5.0.6 with Python 3.8
- SQLite database (db.sqlite3)
- WhiteNoise for static file serving
- Standard Django function-based views

## Build Commands

### Running the Development Server
```bash
cd myshop
python manage.py runserver
```

### Running a Single Test
```bash
cd myshop
python manage.py test shop.tests.TestCaseName.test_method_name
```

### Running All Tests
```bash
cd myshop
python manage.py test
```

### Creating Migrations
```bash
cd myshop
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
cd myshop
python manage.py collectstatic
```

### Django System Check
```bash
cd myshop
python manage.py check
```

## Recommended Linting/Code Quality Tools

Since this project lacks linting configuration, install and use these tools:

```bash
pip install flake8 black isort
```

### Running Linters
```bash
# Format code with Black
black myshop/

# Sort imports with isort
isort myshop/

# Run flake8
flake8 myshop/
```

### Running a Single File Check
```bash
flake8 myshop/shop/views.py
black --check myshop/shop/models.py
```

## Code Style Guidelines

### General Python Style (PEP 8)
- Use 4 spaces for indentation (NO tabs)
- Maximum line length: 88 characters (Black default)
- Use snake_case for function and variable names
- Use PascalCase for class names
- Use SCREAMING_SNAKE_CASE for constants

### Imports
Organize imports in the following order (use isort to enforce):
1. Standard library imports
2. Third-party imports
2. Django imports
4. Local application imports

```python
# Correct import order:
import os
import re
from datetime import datetime

from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail
from django.shortcuts import render

from .models import ContactForm, Post
from .forms import CForm
```

### Models
- Define `Meta` class with `ordering` for consistent query results
- Always implement `__str__` method returning a meaningful string
- Use explicit `on_delete` parameters for ForeignKey fields
- Use appropriate field types and max_length

```python
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
```

### Views
- Use explicit return statements
- Pass context as a dictionary to templates
- Use redirect for navigation after form submissions
- Consider using class-based views for complex views

```python
def contact(request):
    if request.method == 'POST':
        form = CForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = CForm()
    
    return render(request, 'contact.html', {'form': form})
```

### Forms
- Use ModelForm for model-backed forms
- Define Meta class with model and fields

### Admin
- Register models with custom ModelAdmin classes for better UX
- Use list_display, list_filter, search_fields for admin lists

### Templates
- Store templates in `shop/templates/shop/`
- Use descriptive template names matching view context

### Error Handling
- Use try/except blocks for file operations and external calls
- Handle form validation errors gracefully
- Return appropriate HTTP responses (HttpResponseNotFound, etc.)

### Type Annotations (Recommended)
Add type hints for better code clarity:
```python
from typing import Dict, Any

def home(request) -> HttpResponse:
    context: Dict[str, Any] = {}
    return render(request, 'index.html', context)
```

### Database
- Always create migrations after model changes
- Use Django ORM methods (filter, exclude, get) instead of raw SQL
- Use select_related and prefetch_related for query optimization

### Security
- Never commit secrets to version control
- Use environment variables for sensitive settings
- Keep DEBUG=False in production
- Validate all user inputs via forms

### File Paths
- Use os.path.join() for path concatenation
- Use BASE_DIR from settings for absolute paths

## Project Structure

```
myshop/
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── requirements.txt       # Python dependencies
├── myshop/                # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── shop/                  # Main application
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── admin.py
    ├── tests.py
    ├── apps.py
    ├── migrations/
    ├── templates/shop/
    └── static/shop/
```

## Key Settings
- ALLOWED_HOSTS: Includes localhost, 127.0.0.1, tradeaidgh.org
- STATIC_ROOT: myshop/static/static_root
- MEDIA_ROOT: myshop/static/media
- Uses email via SMTP with Gmail

## Testing Best Practices
- Write tests in `shop/tests.py` using Django's TestCase
- Test models, views, forms, and URLs
- Use Django's test client for view testing
- Run tests before committing code
