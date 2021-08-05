# -*- coding utf-8 -*-
"""WSGI-framework

This module demonstrates my skills in creating WSGI-framework.
It's will be the framework like Django or Flask frameworks.
And obviously that project was done for demonstration some of my skills,
wich I obtained when study Python in the GeekBrains university.
"""

import quopri
from framework_requests import GetRequests

class PageNotFound404:
    """This class raise Error 404 if page is not exist"""

    def __call__(self):
        return '404 WAT', '404 PAGE NOT FOUND'


class Framework:
    """This is the main class - the base of WSGI-framework"""

    def __init__(self, routes_obj):
        self.routes_lst = routes_obj

    def __call__(self, environ, start_response):
        # get the address to which the user made the transition
        path = environ['PATH_INFO']

        # add a closing tag
        if not path.endswith('/'):
            path = f'{path}/'

        # obtain all request data
        method = environ['REQUEST_METHOD']
        reauest['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'We obtain post-request: {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'We obtain get-params: {request_params}')

        # find the required controller
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()

        # start the controller
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('UTF-8')]

