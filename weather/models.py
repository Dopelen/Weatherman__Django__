from django.db import models

class CitySearch(models.Model):
    city_name = models.CharField(max_length=100)
    search_count = models.IntegerField(default=0)

    def __str__(self):
        return self.city_name