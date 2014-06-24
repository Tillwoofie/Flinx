import flinx_exceptions as fex
class Flinx_Config(object):
	'''
	A class to structure the config file for Flinx
	'''
	def __init__(self, conf_file = "config"):
		'''
		Importing the config.
		conf_file is the module name of the config.
		'''
		self.flinx_conf = conf_file
		self.modules = None
		self.sys_modules = None
		self.config = {}
		self.parse_config()

	def parse_config(self):
		'''
		Imports the config file (a python file), and parses
		out the required sections for running.
		'''
		from importlib import import_module
		#import Flinx.config as fconf
		import_error = False
		try:
			fconf = import_module("Flinx.{}".format(self.flinx_conf))
		except ImportError:
			import_error = True
		if import_error:
			raise fex.Config_Missing_Exception("cannot find {}.".format(self.flinx_conf))
		#ensure needed sections are present.
		# needed sections are: sys-modules, modules. Even if they are just empty.
		sections = fconf.conf.keys()
		if 'sys_modules' not in sections:
			raise fex.Config_Missing_Exception("sys_modules")
		if 'modules' not in sections:
			raise fex.Config_Missing_Exception("modules")
		#start pulling config in.
		#save the place of the basic modules
		self.modules = fconf.conf['modules']
		self.sys_modules = fconf.conf['sys_modules']
		#pull in all the non-module config
		for x in fconf.conf.keys():
			if x == 'sys_modules':
				continue
			if x == 'modules':
				continue
			self.config[x] = fconf.conf[x]
			
def import_mods(config, sys=False):
	from importlib import import_module
	imported = {}
	if not sys:
		# do le imports
		for x in config.modules:
			imported[x] = import_module("Flinx.plugins.{}".format(x)).main
	else:
		# doesn't support loading system modules yet.
		for x in config.sys_modules:
			imported[x] = import_module("Flinx.sysplugins.{}".format(x)).Config(**config.config[x])
			#stderr_log("imported[x] = import_module(\"Flinx.sysplugins.{}\"".format(x))
	return imported

def stderr_log(msg):
	import sys
	sys.stderr.write("INFO_LOG: {}\n".format(msg))
