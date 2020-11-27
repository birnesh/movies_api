from django.db import models


class Person(models.Model):
    """
    This model contains the info about the a person
    """

    id = models.AutoField(primary_key=True)

    full_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=25, null=True)
    gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    nationality = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{str(self.id)} : {self.full_name}"

    class Meta:
        db_table = "person"
        unique_together = ["full_name", "date_of_birth"]
        verbose_name = "person"
        verbose_name_plural = "person"


class MovieInformation(models.Model):
    """
    This model contains the movie information
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    journal = models.CharField(max_length=30)
    date_of_release = models.DateField()
    imbd_rating = models.FloatField(null=True)
    comic = models.CharField(max_length=10)
    director = models.ForeignKey(
        Person, related_name="directed_movies", on_delete=models.SET_NULL, null=True
    )
    cast = models.ManyToManyField(
        Person, through="CastInformation", related_name="movie_info"
    )

    def __str__(self):
        return f"{str(self.id)} : {self.title}"

    class Meta:
        db_table = "movie_info"
        verbose_name = "movie_info"
        verbose_name_plural = "movie_info"


class CastInformation(models.Model):
    """
    this model cotains the crew and cast in a movie
    """

    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20)
    cast = models.ForeignKey(Person, related_name="cast_info", on_delete=models.CASCADE)
    movie = models.ForeignKey(
        MovieInformation, related_name="cast_info", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{str(self.id)} : {self.title}-{self.cast.name}"

    class Meta:
        db_table = "cast_info"
        verbose_name = "cast_info"
        verbose_name_plural = "cast_info"
