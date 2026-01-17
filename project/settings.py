import os
from pathlib import Path

import dj_database_url 
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

# Загрузка переменных среды из файла
load_dotenv(BASE_DIR / ".env")


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = []

INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS = [
    # Мои приложения
    "apps.blog.apps.BlogConfig",
    "apps.pages.apps.PagesConfig",
    "apps.users.apps.UsersConfig",
    # Third-party приложения
    "mdeditor",
    "markdownify",
    # Системные приложения
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = [
    # Third-party
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # Системные
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
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
                "utils.context_processors.categories",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    

# Настройки аутентификации
AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

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

# Статические файлы
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Этот код может вызывать неполдки в DEBUG режиме
if not DEBUG:
    # Название папки должно быть обязательно таким для деплоя на render.com
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
    
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Медиа-папка
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
        
        # Другое
        'emoji': True,
    }
}

# Для загрузки картинок в MDEDITOR
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Настройки md-рендеринга
MARKDOWNIFY = {
    "default": {
        "MARKDOWN_EXTENSIONS": [
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
        ],
        "WHITELIST_TAGS": [
            "p", "h2", "h3", "h4", "ul", "ol", "li", "img",
            "strong", "em", "a", "code", "pre", "blockquote"
        ],
        "WHITELIST_ATTRS": ["href", "src", "alt", "title",],
    }
}
