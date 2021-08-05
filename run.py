from wsgiref.simple_server import make_server
from own_framework.main import Framework
from urls import routes

# create object of WSGI-application
application = Framework(routes)

with make_server('', 8080, application) as httpd:
    print('Run on the port 8080...')
    httpd.serve_forever()

