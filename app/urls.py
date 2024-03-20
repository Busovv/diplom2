from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.settings import MEDIA_ROOT, MEDIA_URL
import main.urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls.urlpatterns)),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

