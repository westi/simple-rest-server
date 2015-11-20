from bottle import Bottle
from rocket import Rocket

my_example_app = Bottle()

@my_example_app.route('/hello')
def hello():
    return "Hello World!"

my_rocket = Rocket( ( '127.0.0.1', 8080, 'self-signed-cert.pem', 'self-signed-cert.pem' ), 'wsgi', { "wsgi_app":my_example_app } )
my_rocket.start()