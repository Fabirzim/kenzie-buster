from django.db import models

# Create your models here.
from django.db import models

from movies_orders.apps import MoviesOrdersConfig

# Create your models here.
class MoviesOrdersConfig(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20, null=True, choices=Ratings.choices, default=Ratings.G
    )
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="movies"
    )

    orders = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="ordered_movies",
    )

    def __repr__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_orders"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_movie_orders"
    )

    def __str__(self) -> str:
        return f"<MovieOrder [{self.id}] - {self.buyed_at}>"
