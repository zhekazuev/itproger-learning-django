Learning Django Tutorials / Building a Django Website with itProger 

# itProger - Learning Django
![alt text](assets/img/app_about.png "App")

Уроки изучения Django / Создание сайта на Джанго по видеокурсу

## Links
[Уроки изучения Django / Создание сайта на Джанго](https://www.youtube.com/watch?v=L-FyeHQwo4U&list=PLDyJYA6aTY1nZ9fSGcsK4wqeu-xaJksQQ)


## Stack

- Django
- TailwindCSS or Bootstrap
- Docker
- Heroku
- GitHub Actions

## Project

Environment variables:

Use GitHub Secrets, Heroku Config Vars or something secrets for ENV 
For Local environments use .env file, like this
```sh
cat .env
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
DJANGO_ALLOWED_HOSTS=127.0.0.1
DJANGO_SECRET_KEY=secret
DJANGO_STATIC_SECRET_KEY=your_space_secret_key
DJANGO_STATIC_ACCESS_KEY_ID=your_space_access_key_id
DJANGO_LOGLEVEL=INFO
DJANGO_DEBUG=True
DJANGO_DATABASE_ENGINE=sqlite3
DJANGO_DATABASE_HOST=sqlite3
DJANGO_DATABASE_PORT=5432
DJANGO_DATABASE_USERNAME=sqlite3_user
DJANGO_DATABASE_PASSWORD=sqlite3_password
DJANGO_DATABASE_NAME=sqlite3_name
DJANGO_STATIC_BUCKET_NAME=your_space_name
DJANGO_STATIC_ENDPOINT_URL=https://nyc3.digitaloceanspaces.com
```

Project structure
```sh
$ cd project_repository_folder/  <- Repo from github
$ django-admin startproject config && mv config src
$ tree
.
├── Dockerfile
├── LICENSE
├── README.md
├── _config.yml   # config for GitHub Pages
├── assets   # project info for README.md 
│   └── img
├── dist   # files for GitHub Pages
│   ├── css
│   ├── img
│   ├── index.html
│   └── style.css
├── heroku.yml   # config for Heroku
├── package-lock.json   # for Docker build
├── package.json   # for Docker build and GitHub Actions
├── src/...   # Django Project Source Code
├── tailwind.config.js   # Config for TailwindCSS
└── venv   # local venv
```


Django Project Structure
```sh
$ cd project_repository_folder/  <- Repo from github
$ django-admin startproject config
$ mv config src
README
LICENSE
.gitignore
src/                  <- project root - django-admin startproject config - and rename to src
├── config/              <- Django root - django-admin startproject config
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── create_rundom_secret.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main   # app with name - main
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── ...
│   └── views.py
├── manage.py
├── news   # app with name - news
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── ...
│   └── views.py
├── static   # static file - tailwind, css with tailwind minify classes
│   ├── css
│   ├── img
│   └── tailwind.css
└── templates   # templates for Django
```
