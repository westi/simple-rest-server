# simple-rest-server
Simple Python REST server using bottle

# Installing

Get yourself setup once you have cloned like so:
```bash
$ make install
```

# Running

After making sure you are in your virtual environment you can run the server as follows

```bash
$ make run-demo
```

# Testing

To test a server is running you can use curl to request the ping endpoint like so

```bash
$ curl -v -k https://localhost:9000/ping
```

Note we intentionally disable the certificate validation checks in curl for this because the cert is self signed.