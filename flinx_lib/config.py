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
		self.config = None

	def parse_config(self):
		'''
		Imports the config file (a python file), and parses
		out the required sections for running.
		'''
		import Flinx.config as fconf
		#ensure needed sections are present.
		# needed sections are: sys-modules, modules. Even if they are just empty.
		sections = fconf.conf.keys()
		if 'sys_modules' not in sections:
			raise fex.Config_Missing_Exception("sys_modules")
		if 'modules' not in sections:
			raise fex.Config_Missing_Exception("modules")
		#start pulling config in.

	
