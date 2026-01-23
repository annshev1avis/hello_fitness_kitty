import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

# Загрузка переменных среды из файла
load_dotenv(BASE_DIR / ".env")


SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "false").lower() == "true"


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", []).split(",")

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
else:
    INTERNAL_IPS = []

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

MIDDLEWARE = [
    # Системные
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
                "utils.context_processors.categories",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Подключение debug-toolbar
if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE +=  ["debug_toolbar.middleware.DebugToolbarMiddleware"]


# Настройки БД
DB_NAME = os.environ.get("DB_NAME")

if DB_NAME:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": os.environ.get("DB_HOST"),
            "PORT": os.environ.get("DB_PORT"),
            "CONN_MAX_AGE": 300,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


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


# Настройки локализации
LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Статические файлы
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"


# Медиа папка
MEDIA_ROOT = BASE_DIR / "media"  # физический путь на сервере, куда будут сохраняться загруженные файлы

MEDIA_URL = "/media/"  # URL-префикс для доступа к медиафайлам


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
            "markdown.extensions.tables",
        ],
        "STRIP": False,  # не удалять теги
        "WHITELIST_TAGS": [
            "p", "h2", "h3", "h4",
            "ul", "ol", "li",
            "img", "strong", "em", "b", "i", "a", 
            "code", "pre", "blockquote", "br", "hr",
            "table", "thead", "tbody", "tr", "th", "td"
        ],
        "WHITELIST_ATTRS": ["href", "src", "alt", "title", "class"],
    }
}
