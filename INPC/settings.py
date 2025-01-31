import os
from pathlib import Path

# Définition du répertoire de base
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète (Utiliser une variable d'environnement en production)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-(1)n9*^=@z=em5)&84om#!p$-)0zlbl&-tp-zf)!l2%b&drm#q')

# Désactiver DEBUG en production
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Sécuriser ALLOWED_HOSTS (ajouter ton IP et ton domaine)
ALLOWED_HOSTS = ['138.201.52.29', 'localhost', '0.0.0.0']  # Allow specific hosts

# Sécuriser CSRF_TRUSTED_ORIGINS pour accepter les requêtes externes
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:23029',
    'http://0.0.0.0:23029',
    'http://138.201.52.29:23029'
]

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestionproduct',
    'accounts',  # Add accounts app
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Fichier de configuration des URLs
ROOT_URLCONF = 'INPC.urls'

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
            BASE_DIR / "accounts" / "templates",
            BASE_DIR / "gestionproduct" / "templates",
        ],
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

# WSGI
WSGI_APPLICATION = 'INPC.wsgi.application'

# Configuration de la Base de Données (PostgreSQL avec Docker)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'mydatabase'),
        'USER': os.getenv('POSTGRES_USER', 'myuser'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'mypassword'),
        'HOST': os.getenv('POSTGRES_HOST', 'db23029'),  # Assure-toi que c'est bien le nom du service Docker
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Configuration des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Langue et fuseau horaire
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Fichiers statiques (collecte pour le déploiement)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuration des fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuration de la session (ajustable selon besoin)
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 1209600  # 2 semaines
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_SECURE = False  # Mettre True si HTTPS activé

# Sécurité (à activer si HTTPS)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False  # Mettre True si HTTPS activé
SESSION_COOKIE_SECURE = False  # True si HTTPS
CSRF_COOKIE_SECURE = False  # True si HTTPS
X_FRAME_OPTIONS = 'DENY'

# Configuration des logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Authentication settings
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Message settings
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Sécurité derrière un proxy (ex: Nginx)
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')

# Définition du champ ID par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
