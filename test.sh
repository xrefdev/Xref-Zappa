#! /bin/bash
nosetests --with-coverage --cover-package=xrefzappa

# For a specific test:
# nosetests tests.tests:TestZappa.test_lets_encrypt_sanity -s
