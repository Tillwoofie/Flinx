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
