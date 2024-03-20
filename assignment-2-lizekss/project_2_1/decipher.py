import sys

from oracle import Oracle_Connect, Oracle_Disconnect, Oracle_Send


def find_padding(c):
    modified = c.copy()
    for i in range(len(c)):
        modified[i] = (c[i] + 1) % 256
        err = Oracle_Send(modified, len(modified) // 16)
        if err == 0:
            return i
    return len(c)


def decipher_ith_byte(c, padding_idx, padding_val, i, msg):
    iv = c[:padding_idx + padding_val]
    pval = min(16, padding_val + i + 1)
    for j in range(padding_idx, len(iv)):
        iv[j] = iv[j] ^ padding_val ^ pval
    for j in range(padding_idx - i, padding_idx):
        iv[j] = iv[j] ^ ord(msg[j - padding_idx + i]) ^ pval

    iv_init = iv[padding_idx - i - 1]
    pval = (padding_val + i + 1) % 17
    for b in range(256):
        iv[padding_idx - 1 - i] = b
        c[:padding_idx + padding_val] = iv
        err = Oracle_Send(c, len(c) // 16)
        if err != 0:
            m = b ^ pval ^ iv_init
            return chr(m)
    return 'x'


def decipher(c):
    padding_idx = find_padding(c)
    padding_val = -padding_idx

    while padding_val < 1:
        padding_val += 16
    # print(padding_idx, padding_val)
    last_block = ''
    for i in range(padding_idx % 16):
        last_block = decipher_ith_byte(c.copy(), padding_idx, padding_val, i, last_block) + last_block
        # print(last_block)
    result = ''
    while True:
        c = c[:-16]
        if len(c) <= 16:
            break
        block = ''
        for i in range(0, 16):
            block = decipher_ith_byte(c.copy(), 16, 0, i, block) + block
        result = result + block
    return result + last_block

def main():
    if len(sys.argv) < 2:
        print("Usage: python decipher.py <filename>")
        sys.exit(-1)

    f = open(sys.argv[1])
    data = f.read()
    f.close()

    ctext = [(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)]

    Oracle_Connect()
    m = decipher(ctext)
    print(m)
    Oracle_Disconnect()


if __name__ == '__main__':
    main()
