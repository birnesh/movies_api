from movies.views import PersonViewSet, MovieListView
from rest_framework import urls, routers, serializers, viewsets
from django.urls import path, include

router = routers.DefaultRouter()
# router.register(r"person", PersonViewSet)


urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list_view"),
    # path("", include(router.urls)),
    # path("movie_add_update/", MovieCreateView.as_view(), name="movie_list_view"),
]