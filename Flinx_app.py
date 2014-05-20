#Test skeleton

def application(environ, start_response):
	import Flinx.flinx_lib.config
	from Flinx.flinx_lib.url_parse import Url_Parse
	config = Flinx.flinx_lib.config.Flinx_Config()

	up = Url_Parse(environ)
	data = "Hello World!\n\n"
	data += "ENVIRON DUMP\n"
	data += dump_environ(environ)
	data += "\nCONFIG_DUMP\n"
	data += dump_config(config)
	data += "\nPARSED URL DUMP\n"
	data += dump_environ(up)
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

def route_request(environ, config):
	'''
	Main function to route requests into different modules.
	'''
	pass
