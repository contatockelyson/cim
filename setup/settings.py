"""
Configurações do projeto Django.

Gerado pelo comando:
django-admin startproject
"""

from pathlib import Path
import dj_database_url
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================================================
# SEGURANÇA
# ======================================================

# Chave secreta do Django
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-cim-temporaria-2026-x8p4m9k2q7v5n3r6t1w0"
)

# Modo de depuração
# True = Desenvolvimento
# False = Produção
DEBUG = os.getenv("DEBUG", "False") == "True"

# Domínios permitidos
ALLOWED_HOSTS = [
    "2.24.98.138",
    "127.0.0.1",
    "localhost",
]

# Domínios confiáveis para CSRF
CSRF_TRUSTED_ORIGINS = [
    "http://2.24.98.138",
    "http://2.24.98.138:8000",
]

# ======================================================
# CLOUDINARY
# ======================================================

# Configuração para armazenamento de imagens
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

# ======================================================
# APLICAÇÕES INSTALADAS
# ======================================================

INSTALLED_APPS = [
    # Apps padrão do Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Apps do projeto
    "apps.galeria.apps.GaleriaConfig",
    "apps.usuarios.apps.UsuariosConfig",

    # Cloudinary
    "cloudinary_storage",
    "cloudinary",
]

# ======================================================
# MIDDLEWARE
# ======================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
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
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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
# ======================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
        )
    }
else:
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

# ======================================================
# IDIOMA E FUSO HORÁRIO
# ======================================================

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

# ======================================================
# CONFIGURAÇÃO AWS (caso utilize)
# ======================================================

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

AWS_DEFAULT_ACL = "public-read"

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}

AWS_LOCATION = "static"

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
}

# ======================================================
# ARQUIVOS ESTÁTICOS
# ======================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "setup", "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ======================================================
# ARQUIVOS DE MÍDIA
# ======================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ======================================================
# SEGURANÇA HTTPS
# ======================================================

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# ======================================================
# CHAVE PRIMÁRIA PADRÃO
# ======================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
