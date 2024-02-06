from resurrection.settings import *


INSTALLED_APPS = [
    'log_in',
]

TEMPLATES[0]['DIRS'].append(settings.BASE_DIR / 'log_in/static/templates')