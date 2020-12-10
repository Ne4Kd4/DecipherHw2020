#!/usr/bin/python3
import click
import aes
import os

@click.command()
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    default=True,
)
@click.option(
    '--input_file',
    '-i',
    required=True,
)
@click.option(
    '--output_file',
    '-o',
    required=True,
)
@click.option(
    '--block-cipher-mode',
    '-m',
    type=click.Choice(["ECB", "CBC", "CTR"]),
    default="CTR",
)
@click.option(
    '--key-name',
    '-k',
    default=""
)
@click.option(
    '--key-length',
    '-l',
    type=click.Choice(["128", "192", "256"]),
    default="128",
)

# This is due soon...school sucks
def main(encrypt, input_file, output_file, block_cipher_mode, key_name, key_length):

    if encrypt:

        key = aes.random_key_generator(int(key_length), key_name)
       
        if key_length == "10":
            AES = aes.AES(key, 10)

        if key_length == "128":
            AES = aes.AES(key, 128)

        elif key_length == "192":
            AES = aes.AES(key, 192)

        elif key_length == "256":
            AES = aes.AES(key, 256)

        if block_cipher_mode == "ECB":
            bcm = aes.ECB(AES)

        elif block_cipher_mode == "CBC":
            bcm = aes.CBC(AES, 16)

        elif block_cipher_mode == "CTR":
            bcm = aes.CTR(AES)

        bcm.cipher(input_file, output_file)
        write_key(key)
        os.remove(input_file)

    # I legitimately don't know why, but every time I decode something
    # I get a bunch of random NULL characters before the last word???
    # I'll come back around to fixing this
    else:
        key = read_key()
        if key == 1:
            print("File key.txt doesn't exists! Can't decrypt without key")
            exit(1)

        key_length = len(key) * 4

        if key_length == 128:
            AES = aes.AES(key, 128)

        elif key_length == 192:
            AES = aes.AES(key, 192)

        elif key_length == 256:
            AES = aes.AES(key, 256)

        else:
            # Merry Christmas!
            print("Key length not valid!")
            exit(1)

        if block_cipher_mode == "ECB":
            bcm = aes.ECB(AES)

        elif block_cipher_mode == "CBC":
            bcm = aes.CBC(AES, 16)

        elif block_cipher_mode == "CTR":
            bcm = aes.CTR(AES)

        bcm.decipher(input_file, output_file)

# sometimes there’s a double cipher; sometimes, you cipher twice.
def read_key():
    fileName = "key.txt"
    try:
        f = open(fileName, "r")
    except IOError:
        return 1
    
    key = f.read()
    f.close()
    os.remove(fileName)
    # did you like the ascii?
    return key

def write_key(key):
    with open("key.txt", "w") as f:
        f.write(key)
        f.close()

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
