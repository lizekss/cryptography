from core import single_xor_decrypt

n = int(input().strip())
encryptions = []
for i in range(n):
    encryptions.append(input().strip())

max = 0
m = ''
for c in encryptions:
    msg, metric = single_xor_decrypt(bytes.fromhex(c))
    if metric > max:
        max = metric
        m = msg

print(m)