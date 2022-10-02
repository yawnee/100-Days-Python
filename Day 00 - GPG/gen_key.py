# Ensure that gnupg is installed on the machine:
# Install GPG & libraries
# sudo apt install gpg
# sudo pip3 install python-gnupg

import gnupg
import os

KEY_PATH = '!!!!!!ADD DIRECTORY HERE!!!!!!'
NAME_EMAIL = '!!!!!!ADD EMAIL HERE!!!!!!'
PASS_PHRASE = 'ADD PASSWORD HERE'
KEY_TYPE = 'RSA'
KEY_LENGTH = 1024


gpg = gnupg.GPG(gnupghome=f'{KEY_PATH}')

gpg.encoding = 'utf-8'

input_data = gpg.gen_key_input(
                name_email = f'{NAME_EMAIL}',
                passphrase = f'{PASS_PHRASE}',
                key_type = f'{KEY_TYPE}',
                key_length = f'{KEY_LENGTH}')

key = gpg.gen_key(input_data)


