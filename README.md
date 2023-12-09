<h1 align="center">Hi, I'm <span style="color:#15B1ED;">Tima</span>
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">A passionate backend developer from Kyrgyzstan 🇰🇬</h3>

# django Auth

## Installation

Clone this repository then go to the project directory.
```bash
git clone https://github.com/orozbekov/django-auth.git
cd django-auth
```

Сreate a .env configuration file and fill in the details
```bash
SECRET_KEY = "" 

DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_PORT = 5432

PG_ADMIN_EMAIL = ""
PG_ADMIN_PASSWORD = ""
```

In a terminal, run the following command in the base directory of this project to start building the Dockerfile
```bash
docker-compose build
```

After the build is complete, enter this command to start the docker container:
```bash
docker-compose up -d
```
Once the containers are running, you can open the project using the URL:
```bash
http://localhost:8000
```
## Running Tests
To run tests, run the following command
```bash
python manage.py test apps/accounts/tests/
```
<h3 align="center">Languages and Tools:</h3>
<p align="center">
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> 
    <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> 
</a> 
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> 
    <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> 
</a>  
<a href="https://www.python.org" target="_blank" rel="noreferrer"> 
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
</a>  
<a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> 
    <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="redis" width="40" height="40"/> 
</a>
</p>