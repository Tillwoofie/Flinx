#Generic module to enable database usage.

import psycopg

class PGSql_Config(object):
	def __init__(self, database=None, user=None, password=None, host=None, port=None):
		'''
		Keeps database information for creation connections with.
		'''
		self.database = database
		self.user = user
		self.password = password
		self.host = host
		self.port = port

