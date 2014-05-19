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
	enc = ""
	for x in fconf.keys():
		enc += "{}: {}\n".format(x,fconf[x])
	return enc

