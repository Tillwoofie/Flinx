#Test skeleton

def application(environ, start_response):
	data = "Hello World!\nEnvironment Dump:\n"
	data += "ENVIRON DUMP\n"
	data += dump_environ(environ)
	data += "CONFIG_DUMP\n"
	data += dump_config()
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

def dump_config():
        import Flinx.flinx_lib.config as fconf
        config = fconf.Flinx_Config()
        enc = ""
        for x in config.config.keys():
                enc += "{}: {}\n".format(x,config.config[x])
		enc += "sys_modules: {}".format(config.config["sys_modules"])
		enc += "modules: {}".format(config.config["modules"])
        return enc
