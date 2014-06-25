class Environ_Parse(object):
	'''
	A class to grab the PEP-0333 environ vars.
	This will contain the non-standard SCHEME variable, however it is not guaranteed to be set to anything.
	Keeps an 
	'''
	def __init__(self, environ):
		self.raw_environ = environ
		self.env = {}
		self.wsgi_var = {}
		self.parse_environ()
		if "QUERY_STRING" in self.env and self.env["QUERY_STRING"] != "":
			# if it exists and isn't blank...
			self.env["PARSED_QUERY"] = self.parse_query()
		else:
			self.env["PARSED_QUERY"] = None


	def parse_query(self):
		args = []
		for part in self.env["QUERY_STRING"].split("&"):
			if "=" in part:
				s = part.split("=")
				args[s[0]] = s[1]
			else:
				args[part] = None #just as a flag, arg present, but not set.
		return args


	def parse_environ(self):
		'''
		Parses out the PEP-0333 vars.
		Does add an extra key SCHEME if it finds any var that contains 'scheme' in it.
		SCHEME not guaranteed to have a value.
		'''
		for key in self.raw_environ.keys():
			store_key = False
			if key == 'REQUEST_METHOD':
				store_key = True
			elif key == 'SCRIPT_NAME':
				store_key = True
			elif key == 'PATH_INFO':
				store_key = True
			elif key == 'QUERY_STRING':
				store_key = True
			elif key == 'CONTENT_TYPE':
				store_key = True
			elif key == 'CONTENT_LENGTH':
				store_key = True
			elif key == 'SERVER_NAME':
				store_key = True
			elif key == 'SERVER_PORT':
				store_key = True
			elif key == 'SERVER_PROTOCOL':
				store_key = True
			elif key.startswith('HTTP_'):
				store_key = True
			elif 'scheme' in key.lower():
				self.env['SCHEME'] = self.raw_environ[key]
			elif key.startswith('wsgi.'):
				self.wsgi_var[key] = self.raw_environ[key]

			#always at the end
			if store_key:
				self.env[key] = self.raw_environ[key]
		if 'SCHEME' not in self.env:
			self.env['SCHEME'] = None

