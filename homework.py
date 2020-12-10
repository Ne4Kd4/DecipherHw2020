#!/usr/bin/python3
import crypt
import click
import aes

@click.option(
    '--key-name',
    '-k',
    default=""
)

# 4D homework prompt:
# assuming 128 key length, translate a given string into its supposed AES key
def main(key_name):
    return string_to_key(key_name)

# final part of homework...
def string_to_key(key_name):
    # use the "supposed" AES random key generator
    # insert given string and length of 128
    # spit out key