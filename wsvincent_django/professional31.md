# Django for Professionals, 3.1

# Create a virtualenv

```
python3.9 -m venv venvdj
source venvdj/bin/activate
pip install --upgrade pip
pip install Django
pip install 
```

## django-admin startproject to create config directory

Note the dot after `config`.

```
mkdir myproject
cd myproject
django-admin startproject config .
```

## Create a CustomUser (p. 42)

`python manage.py startapp accounts`

Edit `accounts/models.py`

```
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
```

Add `accounts` to `INSTALLED_APPS` in `config/settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...

    'accounts',
]

...
# add at the end
AUTH_USER_MODEL = 'accounts.CustomUser'
```

Make a migration file and migrate:

`python manage.py makemigrations`

`python manage.py migrate`

Create a superuser:

`python manage.py createsuperuser`

## Pages App (p. 51)

`python manage.py startapp pages`

Add `pages` to `INSTALLED_APPS`

Gather all templates in the `myproject/templates` directory

Edit `'DIRS': []` in `TEMPLATES` in `settings.py`:

```
TEMPLATES = [
    {
        ...
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        ...
    }
]
```

## Project-level urls.py

Edit `config/urls.py` to include the `urls.py` in the pages app:

```
from django.contrib import admin
from django.urls import path, include  # add include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

Edit `pages/urls.py`:

```
from django.urls import path
from .views import HomePageView


app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```

Edit `pages/views.py`:

```
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
```

Create a `home.html` page in `templates/`:

```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My Project Home Page</title>
    </head>
    <body>
        <p>This is my home page</p>
    </body>
</html>
```

## Testing

Use `TestCase` because we are running database queries. `SimpleTestCase` is a subset that is designed for sites without models.