"""
Django settings for buses project.
Generated by 'django-admin startproject' using Django 3.0.8.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ncvn$%5pvewazmo)m&6xck96ek!gq79d404=$ej#j457*$x@6_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# En desarollo no hay ALLOWED_HOST, estos solo se definen en secrets.py para producción
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'inicio.apps.InicioConfig',
    'rutas.apps.RutasConfig',
    # 'noticias.apps.NoticiasConfig',
    'empresa.apps.EmpresaConfig',
    'comunidades.apps.ComunidadesConfig',
    'contacto.apps.ContactoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'shapeeditor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'buses.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'buses.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-CR'

TIME_ZONE = 'America/Costa_Rica'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email basic configuration:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

## Shapeeditor
LOGIN_URL='/admin/login/'

#//       +++++++++
#//       +       +
#//       +  Map  +
#//       +       +
#// --->  @++++++++

#// ++++++++@ <---
#// +       +
#// +  Map  +
#// +       +
#// +++++++++
SHAPEEDITOR_MAP_EXTENT_AREA = [[-84.43669241118701, 9.726525930153954],[-83.72894500499169, 9.99625455768836]]

SHAPEEDITOR_MAP_CENTER = [-84.1027104, 9.865107]
#SHAPEEDITOR_ROUTING_MACHINE_URL = "http://router.project-osrm.org/route/v1/driving/" # internal default (demo)
SHAPEEDITOR_ROUTING_MACHINE_URL = "http://161.35.54.122:5000/route/v1/driving/" # costa rica

## Rutas section
# Restricción del mapa a esta área
RUTAS_MAP_MAX_BOUNDS = "[[9.766885, -84.219248], [9.971565, -84.013859]]"

## Load secrets
if os.path.exists(os.path.join(BASE_DIR, 'buses/secrets.py')):
    from buses.secrets import *
