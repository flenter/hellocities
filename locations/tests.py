from django.test import TestCase

from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry

from locations.models import Location


class LocationTestCase(TestCase):
    fixtures = ["data/locations.json"]

    def test_find_cities(self):
        # not really a test... just seeing if there are two items
        self.assertEqual(Location.objects.count(), 2)

    def test_distances(self):

        # "Random" point 0,0 latitude/longitude
        p = GEOSGeometry('POINT(0 0)')

        # Select all locations within the diameter of earth
        ls = Location.objects.filter(geom__distance_lte=(p, D(km=40000)))
        self.assertEqual(ls.count(), 2)

        # Select a city less than 6000 km's away (AMS)
        ls = Location.objects.filter(geom__distance_lte=(p, D(km=6000)))
        self.assertEqual(ls.count(), 1)

        sf = ls[0]

        # Select a city more than 6000 km's away (SF)
        ls = Location.objects.filter(geom__distance_gte=(p, D(km=6000)))
        self.assertEqual(ls.count(), 1)

        ams = ls[0]
        self.assertNotEqual(sf, ams)

from locations.templatetags import distance


class DistanceFilterCase(TestCase):
    fixtures = ["data/locations.json"]

    def test_find_distance(self):
        a, b = Location.objects.all()

        result = distance.calc_distance(a, b)
        self.assertEqual(result, 8794.624631776502)

        self.assertRaises(TypeError, distance.calc_distance, a, 1)
        self.assertRaises(TypeError, distance.calc_distance, 1, b)

        result = distance.calc_distance(b, a)
        self.assertEqual(result, 8794.624631776502)
