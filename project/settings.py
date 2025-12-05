import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

# Загрузка переменных среды из файла
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"


ALLOWED_HOSTS = []


INSTALLED_APPS = [
    # Мои приложения
    "apps.blog.apps.BlogConfig",
    "apps.pages.apps.PagesConfig",
    # Third-party приложения
    "mdeditor",
    # Системные приложения
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "media"  # физический путь на сервере, куда будут сохраняться загруженные файлы

MEDIA_URL = "/media/"  # URL-префикс для доступа к медиафайлам

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Настройки md-редактора
MDEDITOR_CONFIGS = {
    'default': {
        # Внешний вид
        'width': '100%',
        'lineWrapping': True,
        'language': 'en',

        # Загрузка изображений
        'upload_image': True,
        'image_folder': 'editor',
        
        # Автосохранение
        'autosave': {
            'enabled': True,
            'delay': 3000,  # ms
            'uniqueId': 'content'
        },
    }
}