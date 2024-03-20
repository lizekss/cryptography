import base64

from core import edit_distance, single_xor_decrypt

buf = input().strip()
buf = base64.b64decode(buf).decode()


def find_keysize(text):
    min = 8
    result = 0

    for k in range(2, 41):
        n_chunks = len(text) // k
        chunks = [text[i * k:(i + 1) * k] for i in range(n_chunks)]
        d = 0
        for i in range(n_chunks - 1):
            d1 = edit_distance(chunks[i], chunks[i + 1]) / k
            d = (d + d1) / 2
        if d <= min:
            min = d
            result = k
    return result


keysize = find_keysize(buf)
blocks = [buf[i:i + keysize] for i in range(0, len(buf), keysize)]
if len(blocks[-1]) < keysize:
    blocks[-1] = blocks[-1].ljust(keysize)

transposed = []
for i in range(keysize):
    transposed.append(''.join([block[i] for block in blocks]))
decryptions = [single_xor_decrypt(t.encode('ascii'))[0] for t in transposed]
res = ''
n = len(decryptions[0])
for i in range(n):
    for t in decryptions:
        res += t[i]
res = res[:len(buf)]
print(res)
