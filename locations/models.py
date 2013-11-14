from django.contrib.gis.db import models


class Location(models.Model):
    name = models.CharField(max_length=150)
    geom = models.PointField()
    objects = models.GeoManager()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return unicode(self.name)

    def get_lat_long(self):
        """Add an easy getter function, which returns the geometry coords in
        latitude longitude order
        """
        return (self.geom.coords[1], self.geom.coords[0])
