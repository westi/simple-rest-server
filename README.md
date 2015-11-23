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
# generate a self-signed ssl cert for testing
$ openssl req -new -x509 -days 5 -nodes -subj '/C=WL/ST=Deck of Cards/L=Palace/CN=127.0.0.1' -out self-signed-cert.pem -keyout self-signed-key.pem
```

# Running

After making sure you are in your virtual environment you can run the server as follows

```bash
# start using the virtual environmanet
$ source venv/bin/activate
$ python example-server.py --listen-on-ip=127.0.0.1 --listen-on-port=9000 --ssl-key=self-signed-key.pem --ssl-cert=self-signed-cert.pem
```