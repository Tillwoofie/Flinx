
# Written by Jeff Hickson (rvbcaboose@gmail.com).
# This file is part of Flinx, a Python web-framework.

# Flinx is free software, and comes with no warranty.
# It is licenced under the GNU GLP v3.
# The full terms of this are available in the LICENCE file,
# in the root of the project, at <http://www.gnu.org/licenses/>,
# or at <https://github.com/Tillwoofie/Flinx/blob/master/LICENCE>


def not_found(*args):
    '''
    Simple reminder that you:
    a) didn't set a default not_found handler.
    b) missed configuring routes
    '''
    return "I have no idea what you're looking for, bro.\nDo you even lift?\n"


class Request_Router(object):
    def __init__(self, not_found_handler=not_found):
        # a route is (domain, path): callback.
        self.routes = {}
        self.not_found = not_found_handler

    def add_route(self, domain, path, callback):
        self.routes[(domain, path)] = callback

    def route_request(self, parsed_env):
        '''
        Takes in the parsed environment.
        Returns a callback to a function to run.
        '''
        for route in self.routes.keys():
            if route_match(route, parsed_env):
                return self.routes[route]
        # return ther fall back not found problem.
        return self.not_found


def route_match(route_key, penv):
    '''
    Implements the route matching logic of the Request Router.
    Currently only supports exact matching, or a single * for any domain.

    Returns True if route matches, False if not.
    '''
    dom, path = route_key
    if dom == '*' or dom == penv.env['SERVER_NAME']:
        if path == penv.env['PATH_INFO']:
            return True
    # fall back, no match.
    return False
