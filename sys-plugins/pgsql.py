#Generic module to enable database usage.

import psycopg

class Config(object):
	def __init__(self, **kwargs):
		'''
		Keeps database information for creation connections with.
		'''
		self.database = kwargs.get('database', 'flinx')
		self.user = kwargs.get('user', 'flinx')
		self.password = kwargs.get('password', 'nada')
		self.host = kwargs.get('host', 'localhost')
		self.port = kwargs.get('port', '5432')

