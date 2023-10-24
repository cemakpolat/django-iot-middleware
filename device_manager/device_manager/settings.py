from pathlib import Path
import os, environ

env = environ.Env()
env.read_env(env.str('ENV_PATH', './env/.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-06#k=onxzp@qj(((ccxlu713#batdn-b)t6t!l=(+r*rti26!&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['localhost', '0.0.0.0','*']


# MQTT Broker settings
MQTT_BROKER_HOST = "mqtt"
MQTT_BROKER_PORT = 1883
MQTT_CENTRAL_TOPIC = "connect"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'devices',
    'channels',
    
]

MIDDLEWARE =[
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'device_manager.urls'

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
# Channels settings
ASGI_APPLICATION = "device_manager.asgi.application"
WSGI_APPLICATION = 'device_manager.wsgi.application'

# MQTT Broker Configurations

MQTT_BROKER_HOST = env('MQTT_BROKER_HOST',default='mqtt')
MQTT_BROKER_PORT = env('MQTT_BROKER_PORT',default=1883)
MQTT_CENTRAL_TOPIC = env('MQTT_CENTRAL_TOPIC',default='connect')


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DJANGO_DB_NAME',default='mariadb'),  # Replace with your database name
        'USER': env('DJANGO_DB_USER',default='user'),  # Replace with your database username
        'PASSWORD': env('DJANGO_DB_PASSWORD',default='password'),  # Replace with your database password
        'HOST': env('DJANGO_DB_HOST',default='db'), # Replace with the database server address if it's not on localhost
        'PORT': '3306',  # Replace with the database server port if it's not the default (3306)
        'OPTIONS': {
            'charset': 'utf8mb4',  # Adjust character set if needed
        }
    }
}

# Database settings (example for PostgreSQL)
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "your_db_name",
#         "USER": "your_db_user",
#         "PASSWORD": "your_db_password",
#         "HOST": "your_db_host",
#         "PORT": "your_db_port",
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Other settings for templates, internationalization, etc.
# ...

# Django Channels Layer (using Redis as a channel layer backend)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
