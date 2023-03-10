import base64
import codecs
import binascii
import zlib
import bz2

# Print banner
def print_header():
    print("""
  _____       _____            _ 
 |  __ \     |  __ \          | |
 | |  | | ___| |  | | __ _  __| |
 | |  | |/ _ \ |  | |/ _` |/ _` |
 | |__| |  __/ |__| | (_| | (_| |
 |_____/ \___|_____/ \__,_|\__,_|  Made by Double
    """)

# Call print_header() to print the banner
print_header()

# Get decoding type
print("Choose decoding type:")
print("1. Base64")
print("2. URL Encoding")
print("3. Hexadecimal")
print("4. Zlib Compression")
print("5. Bzip2 Compression")

decoding_type = input("Enter decoding type number: ")

# Get encoded code to decode
encoded_code = input("Enter encoded code: ")

# Decode based on chosen type
if decoding_type == "1":
    decoded_code = base64.b64decode(encoded_code).decode("utf-8")
elif decoding_type == "2":
    decoded_code = codecs.decode(encoded_code, 'unicode_escape')
elif decoding_type == "3":
    decoded_code = binascii.unhexlify(encoded_code).decode("utf-8")
elif decoding_type == "4":
    decoded_code = zlib.decompress(encoded_code.encode("utf-8")).decode("utf-8")
elif decoding_type == "5":
    decoded_code = bz2.decompress(base64.b64decode(encoded_code)).decode("utf-8")
else:
    print("Invalid decoding type.")
    exit()

# Print decoded code
print("Decoded code:")
print(decoded_code)
