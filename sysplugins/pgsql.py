#Generic module to enable database usage.

import psycopg2

class Config(object):
	def __init__(self, **kwargs):
		'''
		Keeps database information for creation connections with.
		'''
		self.mod_name = "pgsql"
		self.database = kwargs.get('database', 'flinx')
		self.user = kwargs.get('user', 'flinx')
		self.password = kwargs.get('password', 'nada')
		self.host = kwargs.get('host', 'localhost')
		self.port = kwargs.get('port', '5432')
		self.conn = self.get_pgsql_connection()
	
	def get_pgsql_connection(self):
		return psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)

	def get_existing_connection(self):
		self.conn.autocommit = False #always make sure ti's returned to the default False.
		return self.conn
