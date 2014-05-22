#Basic template for a debug 

def main(environ, parsedUrl, config):

	data = "Hello World!\n\n"
	data += "ENVIRON DUMP\n"
	data += dump_dict(environ)
	data += "\nCONFIG_DUMP\n"
	data += dump_config(config)
	data += "\nPARSED URL DUMP\n"
	data += dump_dict(parsedUrl.env)
	data += "\nWSGI VARS\n"
	data += dump_dict(parsedUrl.wsgi_var)
	return data

def dump_dict(environ):
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

