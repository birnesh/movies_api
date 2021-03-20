from django.contrib import admin
from .models import MovieInformation, Person

admin.site.register(Person)

admin.site.register(MovieInformation)
