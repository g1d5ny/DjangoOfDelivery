"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import pymysql
import dj_database_url

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '64*8t#*g2&eaor0e#qe#r+)o(pm4il_x!5by&#m$-a%d=b+rt@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'shop',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.naver',
    'cart',
    'point',
    'order',
    'django.contrib.sites',
    'storages',
    'disqus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 추가
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',  # base.html에 cart 정보 전달 위해
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# 'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'onlineshop',
#     'USER': 'root',
#     'PASSWORD': '',  # !!! 자신의 비밀번호로 변경
#     'HOST': 'localhost',  # 'onlineshop.csfyvlroglcs.ap-northeast-2.rds.amazonaws.com' 'PORT': '3306',
#     'OPTIONS': {
#         'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO'",
#     },
# DATABASE 변수 이후에 추가해야 함
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

DISQUS_WEBSITE_SHORTNAME = 'DjangoOfDelivery-jungjw'  # Disqus 사이트에 작성한 이름을 써야함
SITE_ID = 1  # sites 앱에 등록된 현재 사이트의 번호, 기본적으로 1번으로 설정

CART_ID = 'cart_in_session'

IAMPORT_KEY = '1297076023466577'
IAMPORT_SECRET = 'BGL66RFf4CZ9mDfBXFfDe2qa9xEReQ2QwOWCGCSLeSUAvacsPs64uxeE4TwiJy9fn6S4IKPXCKx8UKBJ'

AWS_ACCESS_KEY_ID = 'AKIAXCXC4GTO6WKSECSK'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'djangoofdelivery-jungjw'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
AWS_S3_FILE_OVERWRITE = False  # 같은 이름 파일이 있는 경우 덮어 쓸지 설정
# 파일 받아갔을 때 cache를 얼마나 유지할 것인지 설정
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'  # 이렇게 설정하지 않으면 외부 접근이 안되서 못보는 경우가 생김
AWS_LOCATION = 'static'

# STATIC_URL = '/static/' --> 위에 정의되 있던 것을 아래 코드로 변경
STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'
