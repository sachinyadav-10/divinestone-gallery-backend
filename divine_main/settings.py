from pathlib import Path
import os, json
# Import JWT settings


BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ALLOWED_HOSTS = ['*']
APPEND_SLASH = False

CSRF_TRUSTED_ORIGINS = json.loads(os.getenv("CSRF_TRUSTED_ORIGINS",'["https://dev-api.lykke.travel"]'))

# ENVIRONMENT = os.getenv('ENVIRONMENT','dev')
env = os.getenv('ENVIRONMENT','dev')

SECRET_KEY = os.getenv('SECRET_KEY','8_ptCy5L5uE5E9vshjforl31LZUlfx1o8_1kRS4')

INSTALLED_APPS = [
    "django.contrib.admin", 
    'django.contrib.contenttypes',

    "django.contrib.sessions",      
    "django.contrib.messages",     
    "django.contrib.staticfiles",

    'django.contrib.auth',
    'rest_framework',
    'corsheaders',
    'framework',
    'common',
    'catalog',
    'customer',
    # 'order',
    # 'payment',
    # 'pricing',
    'review',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware',  

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middlewares.logging_middleware.LoggerMiddleware',
    'framework.middlewares.response_middleware.ResponseMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False

if env == 'prod':
    CORS_ORIGIN_WHITELIST = (
            'https://dev-operators.lykke.travel',
            'https://operators.lykke.travel',
            'https://dev-creators.lykke.travel',
            'https://creators.lykke.travel')
else:
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
        'https://dev-operator.lykke.travel',
        'https://dev-creator.lykke.travel'
    )
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r'^https://[\w-]+\.ngrok-free\.app$',
    ]

ROOT_URLCONF = 'divine_main.urls'
WSGI_APPLICATION = 'divine_main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
            ],
        },
    },
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'common.handlers.custom_exception_handler',
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'divine_main-static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add JWT settings to globals
PROTON_SERVICE_API_TOKEN = os.getenv('PROTON_SERVICE_API_TOKEN', '')

OPERATOR_JWT_SECRET_KEY = os.getenv('OPERATOR_JWT_SECRET_KEY','8_Zwfyushbty5L5E9v6INyorl31LZUlfx1o8_1kRS4')
OPERATOR_JWT_ALGORITHM = os.getenv('OPERATOR_JWT_ALGORITHM','HS512')
OPERATOR_JWT_ACCESS_TOKEN_EXPIRATION_TIME = 24 * 60 * 60  # 24 hours
OPERATOR_JWT_REFRESH_TOKEN_EXPIRATION_TIME = 24 * 60 * 60 * 30 # 30 days

CREATOR_JWT_SECRET_KEY = os.getenv('CREATOR_JWT_SECRET_KEY','8_Zwfyushbty5L5E9v6INyorl31LZUlfx1o8_1kRS4')
CREATOR_JWT_ALGORITHM = os.getenv('CREATOR_JWT_ALGORITHM','HS512')
CREATOR_JWT_ACCESS_TOKEN_EXPIRATION_TIME = 24 * 60 * 60  # 24 hours
CREATOR_JWT_REFRESH_TOKEN_EXPIRATION_TIME = 24 * 60 * 60 * 30 # 30 days

EMPLOYEE_JWT_SECRET_KEY = os.getenv('EMPLOYEE_JWT_SECRET_KEY','8_kjkfjshtCy5L5uE5E9v6INyorio1LZUlfx1o8_1kRS4')
EMPLOYEE_JWT_ALGORITHM = os.getenv('EMPLOYEE_JWT_ALGORITHM','HS512')
EMPLOYEE_JWT_ACCESS_TOKEN_EXPIRATION_TIME = 24 * 60 * 60  # 24 hours
EMPLOYEE_JWT_REFRESH_TOKEN_EXPIRATION_TIME = 24 * 60 * 60 * 30 # 30 days

IS_OTP_ENABLED = os.getenv('IS_OTP_ENABLED', 'false').lower() == 'true'
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'Travel LYKKE <noreply@lykke.travel>')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY', '')
GOOGLE_PLACES_API_KEY = os.getenv('GOOGLE_PLACES_API_KEY', '')
GOOGLE_PLACES_BASE_URL = os.getenv('GOOGLE_PLACES_BASE_URL', 'https://places.googleapis.com/v1')

N8N_WEBHOOK_BASE_URL = os.getenv('N8N_WEBHOOK_BASE_URL', 'https://n8n.ai.travellykke.com/webhook/')
N8N_API_KEY = os.getenv('N8N_API_KEY', '')
N8N_TIMEOUT = int(os.getenv('N8N_TIMEOUT', '360'))

N8N_IG_LIST_POSTS_DEFAULT_COUNT = int(os.getenv('N8N_IG_LIST_POSTS_DEFAULT_COUNT', '25'))
CONTENT_AUTO_APPROVE_ENABLED = os.getenv('CONTENT_AUTO_APPROVE_ENABLED', 'true').lower() == 'true'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'ap-south-1')

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))
REDIS_DECODE_RESPONSES = os.getenv('REDIS_DECODE_RESPONSES', 'true').lower() == 'true'

OPERATOR_DASHBOARD_URL = os.getenv('OPERATOR_DASHBOARD_URL', 'http://localhost:3000')
CREATOR_DASHBOARD_URL = os.getenv('CREATOR_DASHBOARD_URL', 'https://dev-creator.lykke.travel')

AWS_PROTON_PUBLIC_STORAGE_BUCKET_NAME = os.getenv('AWS_PROTON_PUBLIC_STORAGE_BUCKET_NAME', 'dev-divine_main-public-assets')
AWS_PROTON_PRIVATE_STORAGE_BUCKET_NAME = os.getenv('AWS_PROTON_PRIVATE_STORAGE_BUCKET_NAME', 'dev-divine_main-private-assets')

MONGO_BASE_URI = os.environ.get('MONGO_CONNECTION_STRING', '')

MONGO_DATABASES = {
    'divine_main_db': 'divine_main',
}

if MONGO_BASE_URI:
    import certifi
    import mongoengine

    for alias, db_name in MONGO_DATABASES.items():
        mongoengine.connect(
            db=db_name,
            host=f'{MONGO_BASE_URI}/{db_name}?retryWrites=true&w=majority',
            alias=alias,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=10000,
        )

if env == 'prod':
    import os
    from logging.handlers import RotatingFileHandler

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(os.getenv('SERVER_LOG_FILE_PATH'), 'application.log'),
                #'maxBytes': 5 * 1024 * 1024,  # 5 MB
                #'backupCount': 100,  # keep up to 5 backup files
                'formatter': 'verbose',
            },
            'error_file': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(os.getenv('SERVER_LOG_FILE_PATH'), 'application_error.log'),
                #'maxBytes': 5 * 1024,  # 5 MB
                #'backupCount': 200,  # keep up to 5 backup files
                'formatter': 'verbose',
            },
        },
        'root': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['error_file'],
                'level': 'ERROR',
                'propagate': False,
            },
        },
    }
