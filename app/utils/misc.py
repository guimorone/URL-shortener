from django.utils import timezone
from app.settings import APP_NAME

now = timezone.now()
current_year = now.year

base_context = {
    "current_year": current_year,
    "app_name": APP_NAME,
}
