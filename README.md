Learning Django Tutorials / Building a Django Website with itProger 

# itProger - Learning Django
Уроки изучения Django / Создание сайта на Джанго по видеокурсу

## Links
[Уроки изучения Django / Создание сайта на Джанго](https://www.youtube.com/watch?v=L-FyeHQwo4U&list=PLDyJYA6aTY1nZ9fSGcsK4wqeu-xaJksQQ)


## Project Structure Example


Example from [there](https://github.com/alexey-goloburdin/django-clean-template)
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
│   ├── settings/
│   │   ├── common.py
│   │   ├── development.py
│   │   ├── i18n.py
│   │   ├── __init__.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── __init__.py
├── configs/
│   ├── apache2_vhost.sample
│   └── README
├── doc/
│   ├── Makefile
│   └── source/
│       └── *snap*
├── manage.py
├── README
├── run/
│   ├── media/
│   │   └── README
│   ├── README
│   └── static/
│       └── README
├── static/
│   └── README
└── templates/
    ├── base.html
    ├── core
    │   └── login.html
    └── README
```

Example from Django-docs
```sh
$ cd project_repository_folder/  <- Repo from github
$ django-admin startproject [projectname]
$ tree
README
LICENSE
.gitignore
[projectname]/                  <- project root - django-admin startproject [projectname]
├── [projectname]/              <- Django root - django-admin startproject [projectname]
│   ├── __init__.py
│   ├── settings/
│   │   ├── common.py
│   │   ├── development.py
│   │   ├── i18n.py
│   │   ├── __init__.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── __init__.py
├── configs/
│   ├── apache2_vhost.sample
│   └── README
├── doc/
│   ├── Makefile
│   └── source/
│       └── *snap*
├── manage.py
├── README
├── run/
│   ├── media/
│   │   └── README
│   ├── README
│   └── static/
│       └── README
├── static/
│   └── README
└── templates/
    ├── base.html
    ├── core
    │   └── login.html
    └── README
```
