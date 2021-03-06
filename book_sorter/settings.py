"""
Django settings for Book Sorter project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from decouple import config
from django.utils.log import DEFAULT_LOGGING

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='4cn68iga94@**2x9vb1f*-104pe%*-u-%#%1wh!r(+mjiza@y$', cast=str)
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'core',
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

ROOT_URLCONF = 'book_sorter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'book_sorter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASE_ENGINE = config('DATABASE_ENGINE', default='django.db.backends.sqlite3', cast=str)
DATABASE_NAME = config('DATABASE_NAME', default='process_manager.sqlite3', cast=str)

if 'sqlite' in DATABASE_ENGINE:
    DATABASE_NAME = os.path.join(BASE_DIR, DATABASE_NAME)

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'HOST': config('DATABASE_HOST', default='localhost', cast=str),
        'NAME': DATABASE_NAME,
        'USER': config('DATABASE_USER', default='admin', cast=str),
        'PASSWORD': config('DATABASE_PASSWORD', default='1234qwer', cast=str),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


# Logging

if config('ENABLE_LOGGING', default=False, cast=bool):
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'django.server': DEFAULT_LOGGING['formatters']['django.server'],
            'verbose-pretty': {
                'format': '%(levelname)s [%(asctime)s] N:%(name)s M:%(module)s P:%(process)d T:%(thread)d\n'
                          'Message: %(message)s',
                'datefmt': '%d/%m/%Y %H:%M:%S %z',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s [%(asctime)s] %(name)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'django.server': DEFAULT_LOGGING['handlers']['django.server'],
            'console': {
                'level': 'WARNING',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file-debug': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 16777216,  # 16MB
                'backupCount': 20,
                'formatter': 'verbose-pretty',
                'filename': os.path.join(BASE_DIR, 'logs/django-debug.log'),
            },
            'file-errors': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 16777216,  # 16MB
                'backupCount': 20,
                'formatter': 'verbose-pretty',
                'filename': os.path.join(BASE_DIR, 'logs/django-errors.log'),
                'filters': ['require_debug_false']
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['console', 'file-debug', 'file-errors'],
            },
            'django.server': {
                'handlers': ['django.server', 'file-debug', 'file-errors'],
                'level': 'WARNING',
                'propagate': False,
            },
        },
    }
