import socket
from bottle import Bottle, request, response
from rocket import Rocket

my_example_app = Bottle( )

# A global handler that runs for all requests
@my_example_app.hook('before_request')
def before_request():
	print request.path
	response.set_header('X-Rocket-Powered', socket.getfqdn())

# Let people test to see if we are alive
@my_example_app.route('/ping')
def hello():
    return "pong"

#Let's go
my_rocket = Rocket( ( '127.0.0.1', 8080, 'self-signed-cert.pem', 'self-signed-cert.pem' ), 'wsgi', { "wsgi_app":my_example_app } )
my_rocket.start()