
# Written by Jeff Hickson (rvbcaboose@gmail.com).
# This file is part of Flinx, a Python web-framework.

# Flinx is free software, and comes with no warranty.
# It is licenced under the GNU GLP v3.
# The full terms of this are available in the LICENCE file,
# in the root of the project, at <http://www.gnu.org/licenses/>,
# or at <https://github.com/Tillwoofie/Flinx/blob/master/LICENCE>

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
