#Test skeleton
import Flinx.flinx_lib.config as fconfig
config = fconfig.Flinx_Config()

from Flinx.flinx_lib.request_router import Request_Router
router = Request_Router()

imported_plugins = fconfig.import_mods(config.modules)
router.add_route('*',"/debug", imported_plugins['debug'])

def application(environ, start_response):
	from Flinx.flinx_lib.environ_parse import Environ_Parse

	penv = Environ_Parse(environ)
	data = router.route_request(penv)(environ, penv, config) #oh my god the syntax



	# blah, always return 200 for now.
	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(data)))
	])
	return iter([data])

def dump_environ(environ):
	enc = ""
	for x in environ.keys():
		enc += "{}: {}\n".format(x, environ[x])
	return enc

def dump_config(config):
        #import Flinx.flinx_lib.config as fconf
        #config = fconf.Flinx_Config()
        enc = ""
        for x in config.config.keys():
                enc += "{}: {}\n".format(x,config.config[x])
		enc += "sys_modules: {}\n".format(config.sys_modules)
		enc += "modules: {}\n".format(config.modules)
        return enc

def route_request(environ, parsedUrl, config):
	'''
	Main function to route requests into different modules.

	Takes in environ and config, but only uses information from parsedUrl
	 (an Environ_Parse instance).
	
	For the time being, it needs to have routes statically configured in here.
	'''
	pass
