import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','change-me')
DEBUG = os.environ.get('DEBUG','1') == '1'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'rest_framework','crowd',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser'],
}

# PayPal config
PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID','')
PAYPAL_SECRET = os.environ.get('PAYPAL_SECRET','')
PAYPAL_API_BASE = os.environ.get('PAYPAL_API_BASE','https://api-m.sandbox.paypal.com')
PUBLIC_BASE_URL = os.environ.get('PUBLIC_BASE_URL','http://localhost:8000')
