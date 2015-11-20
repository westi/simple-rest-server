# simple-rest-server
Simple Python REST server using bottle

# Installing

Get yourself setup once you have cloned like so:
```bash
# Create a virtual environment called venv
$ virtualenv venv
# start using the virtual environmanet
$ source venv/bin/activate
$ pip install -r requirements.txt
# generate a self-signed ssl cert
$ openssl req -new -x509 -days 5 -nodes -out self-signed-cert.pem -keyout self-signed-cert.pem
```

