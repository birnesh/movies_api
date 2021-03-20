from rest_framework import serializers
from movies.models import Person, MovieInformation


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieInformation
        fields = [
            "id",
            "title",
            "journal",
            "date_of_release",
            "imbd_rating",
            "comic",
            "director",
            "budget",
        ]
