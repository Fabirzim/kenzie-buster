from rest_framework import serializers
from movies.models import Movie, Ratings, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        allow_null=True, choices=Ratings.choices, default=Ratings.G
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(allow_null=True, read_only=True)
    buyed_at = serializers.DateTimeField(allow_null=True, read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)

    def get_title(self, obj):
        title = obj.movie.title
        return title

    def get_buyed_by(self, obj):
        buyed_by = obj.user.email
        return buyed_by

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
