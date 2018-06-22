from django.test import TestCase
from ..models import Country


class CountryTest(TestCase):
    """
    Test class for country model
    """
    def setUp(self):
        Country.objects.create(
            name="Ghana",
            flag="https://res.cloudinary.com/py/image/upload/v1529641548/ghana-flag-round-small_om6wss.png",
            currency="GHS",
            iso_code="GHS",
        )

    def test_country_name(self):
        ghana = Country.objects.get(name="Ghana")
        self.assertEqual(ghana.name, "Ghana")


