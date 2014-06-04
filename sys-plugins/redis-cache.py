#Generic module to enable redis usage

import redis


class Redis_Config(object):
	def __init__(self, **kwargs):
		'''
		Contains the variables to instantiate some redis connections.
		This class expects host, port and db config values in it's arguments, 
		does not search for others.
		'''
		self.host = kwargs.get('host', 'localhost')
		self.port = kwargs.get('port', '6379')
		self.db = kwargs.get('db', '0')
