#Test skeleton

def application(environ, start_response):
	data = "Hello World!\nEnvironment Dump:\n"
	data += dump_environ(environ)
	start_response("200 OK", [
		("Content-Type", "text/plain"),
		("Content-Length", str(len(data)))
	])
	return iter([data])

def dump_environ(environ)
	enc = ""
	for x in environ.keys():
		enc += "{}: {}\n".format(x, environ[x])
	return enc
