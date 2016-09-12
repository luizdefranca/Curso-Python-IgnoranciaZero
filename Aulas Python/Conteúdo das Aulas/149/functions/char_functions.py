import sys

__author__ = 'pedro'


def enc_print(string, encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')
