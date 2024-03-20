import sys

from oracle import Oracle_Connect, Oracle_Disconnect, Mac


def forge(msg):
    n = len(msg) // 16
    blocks = [msg[i * 16:(i + 1) * 16] for i in range(n + 1)]
    result = bytearray(16)
    for i in range(n):
        if i % 2 == 0:
            x = ''.join(chr(b) for b in xor(result, blocks[i].encode()))
            result = Mac(x + blocks[i + 1], 32)
    return result.hex()


def xor(a, b):
    result = bytearray()
    n = len(a)
    if n > len(b):
        n = len(b)
    for i in range(n):
        c1 = a[i]
        c2 = b[i]
        result.append(c1 ^ c2)
    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python forge.py <filename>")
        sys.exit(-1)

    f = open(sys.argv[1])
    data = f.read()
    f.close()

    Oracle_Connect()

    signature = forge(data)
    print(signature)
    Oracle_Disconnect()


if __name__ == '__main__':
    main()
