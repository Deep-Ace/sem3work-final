import django

import pytest
from .settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sem3work_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmen.EmailBackend'

# pip install pytest
# pip install pytest-django
# pip install git+git://github.com/mverteuil/pytest-ipdb.git
# pip install pytest-cov
# deactivate


# pip install mixer
# 