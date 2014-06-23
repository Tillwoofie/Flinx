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
		self.conn_pool = self.get_redis_conn_pool()
		self.conn = self.get_redis_conn()

	def get_redis_conn_pool(self):
		'''
		Create a new connection pool to use.
		'''
		return redis.ConnectionPool(host=self.host, port=self.port, db=self.db)

	def get_redis_conn(self, conn_pool):
		'''
		Simply creates a new connection in the class's connection pool.
		'''
		return self.redis.StrictRedis(connection_pool=conn_pool)
	
	def get_existing_connection(self):
		return self.conn
