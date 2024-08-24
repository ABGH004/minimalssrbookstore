from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MinLengthValidator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    identity_code = models.CharField(
        max_length=10, unique=True, validators=[MinLengthValidator(10)]
    )

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])


class Book(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.author.id, "pk2": self.id})
