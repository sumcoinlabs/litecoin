#!/usr/bin/env python3
# Copyright (c) 2015-2018 The Litecoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from argparse import ArgumentParser
from base64 import urlsafe_b64encode
from binascii import hexlify
from getpass import getpass
from os import urandom

import hmac

def generate_salt(size):
    """Create size byte hex salt"""
    return hexlify(urandom(size)).decode()

def generate_password():
    """Create 32 byte b64 password"""
    return urlsafe_b64encode(urandom(32)).decode('utf-8')

def password_to_hmac(salt, password):
    m = hmac.new(bytearray(salt, 'utf-8'), bytearray(password, 'utf-8'), 'SHA256')
    return m.hexdigest()

def main():
<<<<<<< HEAD
    parser = ArgumentParser(description='Create login credentials for a JSON-RPC user')
    parser.add_argument('username', help='the username for authentication')
    parser.add_argument('password', help='leave empty to generate a random password or specify "-" to prompt for password', nargs='?')
    args = parser.parse_args()

    if not args.password:
        args.password = generate_password()
    elif args.password == '-':
        args.password = getpass()

    # Create 16 byte hex salt
    salt = generate_salt(16)
    password_hmac = password_to_hmac(salt, args.password)

    print('String to be appended to litecoin.conf:')
    print('rpcauth={0}:{1}${2}'.format(args.username, salt, password_hmac))
    print('Your password:\n{0}'.format(args.password))
=======
    if len(sys.argv) < 2:
        sys.stderr.write('Please include username (and an optional password, will generate one if not provided) as an argument.\n')
        sys.exit(0)

    username = sys.argv[1]

    salt = generate_salt()
    if len(sys.argv) > 2:
        password = sys.argv[2]
    else:
        password = generate_password()
    password_hmac = password_to_hmac(salt, password)

    print('String to be appended to litecoin.conf:')
    print('rpcauth={0}:{1}${2}'.format(username, salt, password_hmac))
    print('Your password:\n{0}'.format(password))
>>>>>>> 28c3cad38365b51883be89e7a306ac7eae1d9ba5

if __name__ == '__main__':
    main()
