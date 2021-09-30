import os
import json
from .get_secrets import get_rds_secret
from storages.backends.s3boto3 import S3Boto3Storage
from decouple import config

ALLOWED_HOSTS = [
    'vidura.com',
]

rds_details: dict = json.loads(get_rds_secret())

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": rds_details.get("username"),
        "PASSWORD": rds_details.get("password"),
        "HOST": rds_details.get("host"),
        "PORT": rds_details.get("port"),
    }
}

# for s3 bucket
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = config('AWS_DEFAULT_ACL')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}


# s3 static settings
class StaticStorage(S3Boto3Storage):
    bucket_name = 'my-app-bucket'
    location = 'static'


STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = StaticStorage


# s3 public media settings
class MediaStorage(S3Boto3Storage):
    bucket_name = 'my-app-bucket'
    location = 'media'


MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = MediaStorage

# # ses email settings
# AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
# AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
#
# AWS_SES_REGION_NAME = os.environ.get('AWS_SES_REGION_NAME')
# AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'

# EMAIL_BACKEND = 'django_ses.SESBackend'
#
# # production settings
# CORS_REPLACE_HTTPS_REFERER = True
# HOST_SCHEME = "https://"
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 1000000
# SECURE_HSTS_PRELOAD = True
