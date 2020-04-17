#!/usr/bin/env python3

import base64
import hashlib
import hmac
import time


def make_digest(message, key):

    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')

    digester = hmac.new(key, message, hashlib.sha1)
    signature1 = digester.digest()

    signature2 = base64.b64encode(signature1)

    return str(signature2, 'UTF-8')


username = input("Username: ")
password = input("Password: ")
#phash = input("Recovered hash: ")
verb = input("HTTP verb: ")
path = input("HTTP path: ")
body = input("HTTP body: ")
date=time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime()) # Wants GMT for some reason.
message=verb + ' ' + path + '\n' + "Date: " + date + '\n' + body

# Skip if using a recovered hash.
key_sha1sum = hashlib.sha1(password.encode('utf-8')).hexdigest()
#key_sha1sum = phash

signature = make_digest(message, key_sha1sum)
print()
print("DATE-AUTH: " + date)
print("AUTHENTICATION: HMAC-SHA1-DATE " + base64.b64encode(bytes(username, 'utf-8')).decode('utf-8') + ":" + signature)
