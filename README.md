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

## Project Structure

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
