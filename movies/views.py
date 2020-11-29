from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets

from movies.models import MovieInformation, Person
from movies.serializers import MovieListSerializer, PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieListView(generics.ListAPIView):
    queryset = MovieInformation.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "title",
        "journal",
        "imbd_rating",
        "comic",
        "director__full_name",
        "budget",
    ]
    search_fields = [
        "title",
        "journal",
        "imbd_rating",
        "comic",
        "director__full_name",
        "budget",
    ]
    ordering_fields = ["date_of_release"]


# class MovieCreateView(generics.CreateAPIView):
#     queryset = MovieInformation.objects.all()
#     serializer_class = MovieListSerializer
