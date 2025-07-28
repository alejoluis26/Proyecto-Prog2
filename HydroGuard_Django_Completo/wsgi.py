
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HydroGuard_Django_Completo.settings")
application = get_wsgi_application()
