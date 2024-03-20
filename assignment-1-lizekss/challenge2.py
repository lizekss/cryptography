buf_1 = input().strip()
buf_2 = input().strip()

i = int(buf_1, 16) ^ int(buf_2, 16)
xor = f'{i:x}'

print(xor)
