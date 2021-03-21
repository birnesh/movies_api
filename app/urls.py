from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from .settings import DEBUG, STATIC_URL 
# from movies import urls as movie_app_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path("movie/", include("movies.urls"))
 ]

if DEBUG:
    urlpatterns += static(STATIC_URL)