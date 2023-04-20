#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value(city_id="33453")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), type(None))

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), type(None))

    def test_description(self):
        """ """
        new = self.value(description="This is a nice place")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), type(None))

    def test_number_bathrooms(self):
        """ """
        new = self.value(number_bathrooms=5)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), type(None))

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), type(None))

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), type(None))

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), type(None))

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
