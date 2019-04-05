from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Bouquet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #
    # What flowers contains in a bouquet
    # flowers = models.CharField(max_length=30)
    #
    price = models.PositiveIntegerField(blank=False)
    image = models.ImageField(upload_to='bouquets')
    #
    # Alternative images for different kinds of flowers
    # image_alt1 = models.ImageField()
    # image_alt2 = models.ImageField()
    # image_alt3 = models.ImageField()
    #
    # popularity = models.PositiveSmallIntegerField(default=0)
    #
    # Validity days count
    # validity = models.PositiveSmallIntegerField()
    #
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
