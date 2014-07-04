# Example conf for Flinx.

# Written by Jeff Hickson (rvbcaboose@gmail.com).
# This file is part of Flinx, a Python web-framework.

# Flinx is free software, and comes with no warranty.
# It is licenced under the GNU GLP v3.
# The full terms of this are available in the LICENCE file,
# in the root of the project, at <http://www.gnu.org/licenses/>,
# or at <https://github.com/Tillwoofie/Flinx/blob/master/LICENCE>

#main conf var.
conf = {}

# what modules to load
sys_modules = ['pgsql', 'redis-cache']
modules = ['debug', 'redis_test', 'pgsql_test']

#postgres config
pgsql = {}
pgsql['user'] = 'flinx'
pgsql['pass'] = 'a_password'
pgsql['address'] = "localhost"
pgsql['port'] = "5432"
pgsql['db'] = "flinx"

#redis config
rc = {}
rc['address'] = "localhost"
rc["port"] = "6379"
rc['db'] = "0"

# add config to pertinent sections.
conf['sys_modules'] = sys_modules
conf['modules'] = modules
conf['pgsql'] = pgsql
conf['redis-cache'] = rc
