from django.contrib import admin
from django.urls import path, include

# from movies import urls as movie_app_url

urlpatterns = [path("admin/", admin.site.urls), path("", include("movies.urls"))]
