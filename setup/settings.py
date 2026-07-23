"""
Configurações do projeto CIM.
Produção na VPS Hostinger.
"""

from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv


# ======================================================
# DIRETÓRIO BASE
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega /root/cim/.env
load_dotenv(BASE_DIR / ".env")


# ======================================================
# SEGURANÇA
# ======================================================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-cim-temporaria-2026-troque-esta-chave"
)

DEBUG = os.getenv("DEBUG", "False").lower() == "true"


ALLOWED_HOSTS = [
    "2.24.98.138",
    "127.0.0.1",
    "localhost",
]


CSRF_TRUSTED_ORIGINS = [
    "http://2.24.98.138",
]


# ======================================================
# APLICAÇÕES
# ======================================================

INSTALLED_APPS = [

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Projeto
    "apps.galeria.apps.GaleriaConfig",
    "apps.usuarios.apps.UsuariosConfig",
]


# ======================================================
# MIDDLEWARE
# ======================================================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    # Arquivos estáticos
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ======================================================
# URLS
# ======================================================

ROOT_URLCONF = "setup.urls"


# ======================================================
# TEMPLATES
# ======================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [

                "django.template.context_processors.debug",
                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ======================================================
# WSGI
# ======================================================

WSGI_APPLICATION = "setup.wsgi.application"


# ======================================================
# BANCO DE DADOS
# PostgreSQL na própria VPS
# ======================================================

DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL:

    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,

            # Reaproveita conexões
            conn_max_age=600,

            # PostgreSQL está na mesma VPS
            ssl_require=False,
        )
    }

else:

    # Fallback apenas para desenvolvimento
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# ======================================================
# VALIDAÇÃO DE SENHAS
# ======================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ======================================================
# IDIOMA / HORÁRIO
# ======================================================

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# ======================================================
# ARQUIVOS ESTÁTICOS
# CSS / JS / ÍCONES
# ======================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# Pasta de arquivos estáticos do projeto
STATICFILES_DIRS = [
    BASE_DIR / "setup" / "static",
]


# ======================================================
# ARMAZENAMENTO
# ======================================================

STORAGES = {

    # Fotos e arquivos enviados pelo usuário
    # Agora ficam fisicamente na VPS
    "default": {
        "BACKEND":
        "django.core.files.storage.FileSystemStorage",
    },

    # CSS / JS
    "staticfiles": {
        "BACKEND":
        "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# ======================================================
# IMAGENS / MEDIA
# ======================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ======================================================
# HTTPS / PROXY
# ======================================================

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https"
)

USE_X_FORWARDED_HOST = True


# Estamos usando HTTP por enquanto.
# Quando configurarmos domínio + HTTPS, mudaremos para True.

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False


# ======================================================
# CHAVE PRIMÁRIA
# ======================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"