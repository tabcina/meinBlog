
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "6d52b488-a053-4288-ae7d-c809297b9c7528a04390-7a64-4739-a3f1-429966479697c6e2319b-bbd6-4119-bf3c-4d9be2a8c607"
NEVERCACHE_KEY = "9a6f3ed0-3cac-4395-a6d7-96350c049deb4b75cc27-f091-4dd8-9a2b-963134ee5742a7f08b89-4a9e-490f-8219-77cfe5ca8ecc"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        #"ENGINE": "django.db.backends.sqlite3",
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        #"NAME": "dev.db",
        "NAME": "postgres",
        # Not used with sqlite3.
        #"USER": "",
        "USER": "postgres",
        # Not used with sqlite3.
        #"PASSWORD": "",
        "PASSWORD": "Tabs123",
        # Set to empty string for localhost. Not used with sqlite3.
        #"HOST": "",
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        #"PORT": "",
        "PORT": "5432"
    }
}

FABRIC = {
 "SSH_USER": "vagrant", # SSH username
 "SSH_PASS": "vagrant", # SSH password (consider key-based authentication)
 #"HOSTS": ['192.168.124.10' ], # List of host names or IPs.
"HOSTS": ['127.0.0.1'],
 "VIRTUALENV_HOME": "/home/vagrant/", # Absolute remote path for virtualenvs
 "PROJECT_NAME": "blog", # Unique identifier for project
 "REQUIREMENTS_PATH": "requirements/requirements.txt", # Path to pip requirements, relative to project
 "GUNICORN_PORT": 8000, # Port gunicorn will listen on
 "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
 "LIVE_HOSTNAME": "example.com", # Host for public site.
 "REPO_URL": "git@github.com:tabcina/meinBlog.git",
 "DB_PASS": "default", # Live database password
 "ADMIN_PASS": "default", # Live admin user password
 "SECRET_KEY": SECRET_KEY
}
