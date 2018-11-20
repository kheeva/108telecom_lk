import os
from dotenv import load_dotenv
project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lk.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

from configurations.management import execute_from_command_line

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
