# TODO: Make this conformant to PEP-0333.
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

class Url_Parse(object):
	'''
	A class to process URLs from the given wsgi environment vars
	to aid in routing requests.
	'''
	def __init__(self, environ, arg_char = '?'):
		self.environ = environ
		self.ssl = False
		self.scheme = None
		self.full_request = None
		self.domain = None
		self.request_path = None
		self.arg_char = arg_char
		self.args = None
		#do the actual parse
		self.parse_environ()
		# map into a dict for sometimes-usefulness
		self.env = {}
		self.env['ssl'] = self.ssl
		self.env['scheme'] = self.scheme
		self.env['full_request'] = self.full_request
		self.env['domain'] = self.domain
		self.env['request_path'] = self.request_path
		self.env['arg_char'] = self.arg_char
		self.env['args'] = self.args
	
	def parse_environ(self):
		'''
		Parse the wsgi environ variable and grab some information.
		'''
		env = self.environ
		#wsgi.url_scheme should be set by the server automatically.
		self.scheme = env.get('wsgi.url_scheme', None)
		if self == 'https':
			self.ssl = True
		self.full_request = "{}{}".format(env.get('HTTP_HOST'), env.get('RAW_URI'))
		self.domain = env.get('HTTP_HOST')
		self.request_path = env.get('RAW_URI')
		#only grab what comes after the arg_char.
		self.args = self.request_path[self.request_path.find(self.arg_char)+1:]
