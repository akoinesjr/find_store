import pdb
import unittest
import configparser
from find_store import StoreFinder

config = configparser.ConfigParser()
config.read('config.ini')
google_key = config.get('config', 'google_key')
address = '1 Market St, San Francisco, CA'
units = 'mi'
output = 'text'

class TestStoreFinder(unittest.TestCase):

	def setUp(self):
		self.StoreFinder = StoreFinder(google_key, address, units, output)

	def test_get_lat_lng(self):
		self.assertEqual(self.StoreFinder.get_lat_lng(address), {'lat': 37.7941181, 'lng': -122.3949838})

	def test_get_distance_between_locations(self):
		loc1 = {'lat': 37.7941181, 'lng': -122.3949838}
		loc2 = {'lat': 27.7941181, 'lng': -112.3949838}
		self.assertEqual(self.StoreFinder.get_distance_between_locations(loc1, loc2), 901.4180474341488)
		self.assertEqual(self.StoreFinder.get_distance_between_locations(loc1, loc2, 'km'), 1450.692174939205)

	def test_get_closest_location(self):
		data = self.StoreFinder.read_csv('store-locations.csv', header=True)
		location = self.StoreFinder.get_lat_lng(address)
		closest = self.StoreFinder.get_closest_location(data, location)
		self.assertEqual(['San Francisco CBD East', 'SWC Bush and Sansome Street', '225 Bush St', 'San Francisco', 'CA', '94104-4251', '37.790841', '-122.4012802', 'San Francisco County'], closest)

if __name__ == '__main__':
	unittest.main()