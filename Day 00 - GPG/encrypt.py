# Ensure that gnupg is installed on the machine:
# Install GPG & libraries
# sudo apt install gpg
# sudo pip3 install python-gnupg

import gnupg
import os

PATH = '!!!!!!ADD DIRECTORY HERE!!!!!!'
NAME_EMAIL = '!!!!!!ADD EMAIL HERE!!!!!!'

gpg = gnupg.GPG(gnupghome = f'{KEY_PATH}')

path = 'path of file you wish to encrypt' # path of file you wish to encrypt
ptfile = 'file you wish to encrypt from path' # file you wish to encrypt from path

with open(path + ptfile, 'rb') as f:
    status = gpg.encrypt_file(f, recipients = [f'{NAME_EMAIL}'], output = path + ptfile + ".encrypted")

print(status.ok)
print(status.stderr)