
# Written by Jeff Hickson (rvbcaboose@gmail.com).
# This file is part of Flinx, a Python web-framework.

# Flinx is free software, and comes with no warranty.
# It is licenced under the GNU GLP v3.
# The full terms of this are available in the LICENCE file,
# in the root of the project, at <http://www.gnu.org/licenses/>,
# or at <https://github.com/Tillwoofie/Flinx/blob/master/LICENCE>

# Test skeleton
import Flinx.flinx_lib.config as fconfig
config = fconfig.Flinx_Config()

from Flinx.flinx_lib.request_router import Request_Router
router = Request_Router()

app_plugins = fconfig.import_mods(config)
sys_plugins = fconfig.import_mods(config, sys=True)
router.add_route('*', "/debug", app_plugins['debug'])
router.add_route('*', "/redis_test", app_plugins['redis_test'])
router.add_route('*', "/pgsql_test", app_plugins['pgsql_test'])


def application(environ, start_response):
    from Flinx.flinx_lib.environ_parse import Environ_Parse

    penv = Environ_Parse(environ)
    # oh my god the syntax
    data = router.route_request(penv)(environ, penv, config, sys_plugins)

    # blah, always return 200 for now.
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
