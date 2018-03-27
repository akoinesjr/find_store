import pdb
import os
import csv
import math
import argparse
import configparser
import json

import requests
import googlemaps

class StoreFinder():

	def __init__(self, google_key, address, units, output):

		self.gmaps = googlemaps.Client(google_key)
		self.address = address
		self.units = units
		self.output = output

	def read_csv(self, filename, header=False, delimiter=','):
		"""
		Returns a list where each element represents a row in a CSV file (or other type of delimited file)
		"""

		results = None
		with open(filename, 'rU') as csvfile:
			csv_reader = csv.reader(csvfile, delimiter=delimiter)
			if header:
				next(csv_reader) #Skip header
			results = [row for row in csv_reader]

		return results

	def get_lat_lng(self, address):
		"""
		Returns the latitude and longitudee for a given address or zip code
		"""

		geocode_data = self.gmaps.geocode(address)
		return geocode_data[0]['geometry']['location']

	def get_distance_between_locations(self, loc1, loc2, units='mi'):
		"""
		Calculates the distance between pairs of lat/lng coordinates using the Haversine formula
		See: https://gist.github.com/rochacbruno/2883505
		"""

		radius = 6371 #km radius of Earth

		dlat = math.radians(float(loc2['lat']) - float(loc1['lat']))
		dlng = math.radians(float(loc2['lng']) - float(loc1['lng']))
		a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(float(loc1['lat']))) \
			* math.cos(math.radians(float(loc2['lat']))) * math.sin(dlng/2) * math.sin(dlng/2)
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		distance = radius * c

		if units == 'km':
			return distance
		elif units == 'mi':
			return distance * .621371
		else:
			raise Exception('Could not calculate distance, units must be either "mi" or "km"!')

	def get_closest_location(self, data, location):

		return min(data, key=lambda x: self.get_distance_between_locations({'lat': x[6], 'lng': x[7]}, location))

	def run(self):

		data = store_finder.read_csv('store-locations.csv', header=True)
		location = self.get_lat_lng(self.address)
		closest = self.get_closest_location(data, location)
		distance = round(self.get_distance_between_locations({'lat': closest[6], 'lng': closest[7]}, location, units), 2)
		if self.output == 'text':
			print("The nearest store is {}, located at {}, {}, {} and is {} {} away from {}".format(closest[0], closest[2], closest[3], closest[4], distance, units, self.address))

		elif self.output == 'json':

			response = {
				'Search Address': self.address,
				'Store Name': closest[0],
				'Nearest Address': closest[2],
				'City': closest[3],
				'State': closest[4],
				'Distance': distance,
				'Units': units
			}

			with open('output.json', 'w') as outfile:
				json.dump(response, outfile)

		else:
			raise Exception('Output must be either "text" or "json"!')

if __name__ == '__main__':

	config = configparser.ConfigParser()
	config.read('config.ini')
	google_key = config.get('config', 'google_key')

	parser = argparse.ArgumentParser(description='')
	group = parser.add_mutually_exclusive_group()
	group.add_argument('--address')
	group.add_argument('--zip')
	parser.add_argument('--units', default='mi')
	parser.add_argument('--output', default='text')

	parsed_args, unknown_args = parser.parse_known_args()

	address = parsed_args.address or parsed_args.zip
	units = parsed_args.units
	output = parsed_args.output

	store_finder = StoreFinder(google_key, address, units, output)

	store_finder.run()

