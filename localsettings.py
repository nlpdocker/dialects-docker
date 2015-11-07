## localsettings.py ##

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

import os#Used to import secret key from environment variable

#####I use an environmental variable for the secret key, but you can use something else.###
SECRET_KEY = os.environ['DIALECTDBSK']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#There are some differences in Middleware between the debug and production versions
MIDDLEWARE_CLASSES = (
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#Different local apps for debug and production versions

LOCAL_INSTALLED_APPS = ('django_extensions',
)

#Debug version settings
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False

TEMPLATE_DEBUG = True

#Make sure you update the User and Password for the database as appropriate.
DATABASES = {
'default': {
'ENGINE': 'django.contrib.gis.db.backends.postgis',
'NAME': 'arabicDialectProject',
'USER': 'postgres',
'PASSWORD': 'postgres',
'HOST': '127.0.0.1',
'PORT': '5432',

}
}


ALLOWED_HOSTS = [
"database-of-arabic-dialects.org"
]

