#Generic module to enable redis usage

import redis


class Config(object):
	def __init__(self, **kwargs):
		'''
		Contains the variables to instantiate some redis connections.
		This class expects host, port and db config values in it's arguments, 
		does not search for others.
		'''
		self.mod_name = "redis-cache"
		self.host = kwargs.get('host', 'localhost')
		self.port = kwargs.get('port', '6379')
		self.db = kwargs.get('db', '0')
