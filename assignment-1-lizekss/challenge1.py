# add your imports here

# reading input (don't forget strip in other challenges!)
import base64

str_hex = input().strip()

str_base64 = base64.b64encode(bytearray.fromhex(str_hex)).decode()

print(str_base64)
