from django.db import models
from products.models import Product

# Create your models here.


class Week(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)
    friendly_name = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class RaceTrack(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Datapack(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    week = models.ForeignKey(Week, null=True, blank=True, on_delete=models.SET_NULL)
    track_name = models.ForeignKey(RaceTrack, null=True, blank=True, on_delete=models.SET_NULL)
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    race_setup = models.FileField(null=True, blank=True, upload_to="datapacks/setups/")
    qual_setup = models.FileField(null=True, blank=True, upload_to="datapacks/setups/")
    telemetry = models.FileField(null=True, blank=True, upload_to="datapacks/telemetry/")
    blap = models.FileField(null=True, blank=True, upload_to="datapacks/lapfiles/")
    olap = models.FileField(null=True, blank=True, upload_to="datapacks/lapfiles/")

    def __str__(self):
        return '%s %s' %(self.product.name, self.week)
