
# Written by Jeff Hickson (rvbcaboose@gmail.com).
# This file is part of Flinx, a Python web-framework.

# Flinx is free software, and comes with no warranty.
# It is licenced under the GNU GLP v3.
# The full terms of this are available in the LICENCE file,
# in the root of the project, at <http://www.gnu.org/licenses/>,
# or at <https://github.com/Tillwoofie/Flinx/blob/master/LICENCE>

# Basic template for a debug


def main(environ, parsedUrl, config, sys_mods):

    pure = bool(get_url_arg("pure", parsedUrl, False))
    body = bool(get_url_arg("body", parsedUrl, False))

    data = "Hello World!\n\n"
    data += "ENVIRON DUMP\n"
    data += dump_dict(environ)
    if not pure:
        data += "\nCONFIG_DUMP\n"
        data += dump_config(config)
        data += "\nDIR\n"
        data += dump_dir(sys_mods)
        data += "\nPARSED URL DUMP\n"
        data += dump_dict(parsedUrl.env)
    data += "\nWSGI VARS\n"
    data += dump_dict(parsedUrl.wsgi_var)

    if not pure or body:
        data += "\nBody Test:\n"
        body_data = parsedUrl.wsgi_var["wsgi.input"].read()
        data += body_data + "\n"

    if not pure:
        data += "\nSys-mods names.\n"
        for x in sys_mods:
            mod = sys_mods[x]  # weird import naming?
            data += "{}\n".format(mod.mod_name)
    return data


def dump_dir(obj):
    out = ""
    for x in obj:
        out += str(dir(x))
        out += "\n"
    return out


def dump_dict(environ):
    enc = ""
    for x in environ.keys():
        enc += "{}: {}\n".format(x, environ[x])
    return enc


def dump_config(config):
        enc = ""
        for x in config.config.keys():
                enc += "{}: {}\n".format(x, config.config[x])
        enc += "sys_modules: {}\n".format(config.sys_modules)
        enc += "modules: {}\n".format(config.modules)
        return enc


def get_url_arg(arg, env, default=None):
    if env.env["PARSED_QUERY"] is not None:
        return env.env["PARSED_QUERY"].get(arg, default)
    else:
        return default
