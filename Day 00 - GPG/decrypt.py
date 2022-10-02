# Ensure that gnupg is installed on the machine:
# Install GPG & libraries
# sudo apt install gpg
# sudo pip3 install python-gnupg

import gnupg
import os

PATH = '!!!!!!ADD DIRECTORY HERE!!!!!!'
PASS_PHRASE = 'DD PASSWORD HERE'

gpg = gnupg.GPG(gnupghome=f'{PATH}')

path = 'path of file you wish to encrypt'  # path of file you wish to encrypt
ptfile = 'file you wish to encrypt from path.encrypted'  # file you wish to encrypt from path

with open(path + ptfile, 'rb') as f:
    status = gpg.decrypt_file(f, passphrase=f'{PASS_PHRASE}', output=path + ptfile + ".decrypted")

print(status.ok)
print(status.stderr)
