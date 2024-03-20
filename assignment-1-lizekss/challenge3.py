from core import single_xor_decrypt

hx = input().strip()

res = single_xor_decrypt(bytes.fromhex(hx))

print(res[0])
