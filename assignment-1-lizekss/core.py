sorted_alphabet = 'zqxjkvbpgfywmcudlrshinoate '


def single_xor_decrypt(buf):
    max = 0
    res = ''
    for k in range(0, 255):
        m = ""
        for b in buf:
            m += chr(b ^ k)
        count = 0

        for c in m:
            if c in sorted_alphabet:
                count += sorted_alphabet.index(c)

        if max < count:
            max = count
            res = m
    return res, max


def repeating_encrypt(k, m):
    c = bytearray()
    k_i = 0
    for b in m:
        c.append(ord(b) ^ ord(k[k_i]))
        k_i = (k_i + 1) % len(k)
    return c.hex()


def edit_distance(a, b):
    a_int = int.from_bytes(a.encode(), "big")
    b_int = int.from_bytes(b.encode(), "big")
    binary = bin(a_int ^ b_int)
    result = 0
    for b in binary:
        if b == '1':
            result += 1
    return result
