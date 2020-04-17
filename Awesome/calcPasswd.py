#!/usr/bin/env python3

# Courtesy of Seagate: http://www.seagate.com/nasos/SDK/0.7/api_ref/Ciphered.html

from Crypto.Cipher import AES
from os import urandom
from hashlib import sha256
from base64 import b64encode, b64decode

secret_key = input('Recovered SHA1 sum: ').encode('ascii')
datas = input('New password: ')


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]
key = sha256(secret_key).digest()
padded = pad(datas)
iv = urandom(16)
cipher = AES.new(key, AES.MODE_OFB, iv)
#output = "%s%s" % (iv, cipher.encrypt(padded))
output = iv + cipher.encrypt(padded)
result = b64encode(output)

print(result.decode('utf-8'))
