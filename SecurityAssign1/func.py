from Crypto.Cipher import AES
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend

import os


def GetCrypCipher(mode):
    backend = default_backend()
    key = os.urandom(32)
    cipher = Cipher(algorithms.AES(key), mode, backend=backend)

    return cipher


def GetCipher(mode, iv='', ctr=''):
    # key (byte string)
    # The secret key to use in the symmetric cipher. It must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) bytes long.
    key = b'_____________________32 byte key'

    if (mode == AES.MODE_CTR):
        ctr = os.urandom(16)
        cipher = AES.new(key, mode, counter=lambda: ctr)

    elif (mode == AES.MODE_CBC):
        cipher = AES.new(key, mode, iv)

    else:
        cipher = AES.new(key, mode)

    return cipher


def GetPlainText():
    PlainTextFile = open('D:/PlainText.txt', 'r')
    PlainText = PlainTextFile.read()
    return PlainText


def Padding(Input):
    return Input + (AES.block_size - len(Input) % AES.block_size) * chr(AES.block_size - len(Input) % AES.block_size)


def WriteFile(path, str):
    fileopen = open(path, 'w')
    fileopen.write(str)
    fileopen.close()
