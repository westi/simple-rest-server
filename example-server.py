import socket
import argparse
import logging
from bottle import Bottle, request, response
from rocket import Rocket

my_argparser = argparse.ArgumentParser()
my_argparser.add_argument( '--listen-on-ip', '-l', required=True )
my_argparser.add_argument( '--listen-on-port', '-p', type=int, required=True )
my_argparser.add_argument( '--ssl-key', required=True )
my_argparser.add_argument( '--ssl-cert', required=True )
my_argparser.add_argument( '--verbose', action='store_true')
parsedargs = my_argparser.parse_args()
my_example_app = Bottle( )

# A global handler that runs for all requests
@my_example_app.hook('before_request')
def before_request():
	response.set_header('X-Rocket-Powered', socket.getfqdn())

# Let people test to see if we are alive
@my_example_app.route('/ping')
def hello():
    return "pong"

#Enable INFO logging?
if parsedargs.verbose:
	log = logging.getLogger('Rocket')
	log.setLevel( logging.INFO )
	log.addHandler(logging.StreamHandler())

#Let's go
my_rocket = Rocket( ( parsedargs.listen_on_ip, parsedargs.listen_on_port, parsedargs.ssl_key, parsedargs.ssl_cert ), 'wsgi', { "wsgi_app":my_example_app } )
my_rocket.start()