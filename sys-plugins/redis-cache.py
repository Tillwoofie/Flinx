#Generic module to enable redis usage

import redis

class Redis_Config(object):
	def __init__(self, host, port, db):
		'''
		Contains the variables to instantiate some redis connections.
		'''
		self.host = host
		self.port = port
		self.db = db
