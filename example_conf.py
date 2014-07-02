# Example conf for Flinx.

#main conf var.
conf = {}

# what modules to load
sys_modules = ['pgsql', 'redis-cache']
modules = ['debug', 'redis_test']

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
