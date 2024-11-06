from .base import *

settings.setenv("development")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = settings.DATABASES

DATABASES["default"]["NAME"] = str(PROJECT_DIR / "db.sqlite3")
