# Dj-Wikipedia


### create virualenv
```
python -m venv venv
```

### activate venv (Windows)
```
venv\Scripts\activate
```

### create .env file
```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=
```

### make django migrations
```
python manage.py makemigrations
python manage.py migrate
```

### run django server
```
python manage.py runserver
```