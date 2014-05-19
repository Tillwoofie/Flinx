class Flinx_Error(Exception):
	'''
	Base Exception for Flinx.
	'''
	pass

class Config_Missing_Exception(Flinx_Error):
	'''
	Defines an exception for missing config.
	'''
	def __init__(self, missing_config):
		self.missing_config = missing_config
		self.value = self.missing_config
	
	def __str__(self):
		return repr(self.missing_config)
