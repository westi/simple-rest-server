# Simple make file to make it easy to repeatable install/build/run/clean up the example server
SHELL=/bin/bash
.PHONY: clean install run-demo nuke-old-certs

# If we have a self-signed-cert and it has expired then we will nuke them so they get regenerated.
maybe-nuke-certs != [[ -f self-signed-cert.pem ]] && openssl verify self-signed-cert.pem | grep "error 10" | sed "s/^.*$$/nuke-old-certs/"

install: srs-virtualenv self-signed-cert.pem

# We need all the commands on one line so they run in the same shell, only rebuild the virtual env if the requirements change
srs-virtualenv: requirements.txt
	# Only initialise the first time
	[[ -d srs-virtualenv ]] || virtualenv srs-virtualenv;
	source ./srs-virtualenv/bin/activate; pip install -r requirements.txt; deactivate
	# ensure we always update the mtime even if no build occurs - this happens if mtime of requirements file changes but content doesn't
	touch srs-virtualenv

nuke-old-certs:
	rm -rf self-signed-cert.pem self-signed-key.pem

clean: nuke-old-certs
	rm -rf *.pyc srs-virtualenv

self-signed-cert.pem: $(maybe-nuke-certs)
	openssl req -new -x509 -days 1 -nodes -subj '/C=WL/ST=Deck of Cards/L=Palace/CN=127.0.0.1' -out self-signed-cert.pem -keyout self-signed-key.pem

run-demo: install
	source ./srs-virtualenv/bin/activate; \
	python example-server.py --listen-on-ip=127.0.0.1 --listen-on-port=9000 --ssl-key=self-signed-key.pem --ssl-cert=self-signed-cert.pem --verbose