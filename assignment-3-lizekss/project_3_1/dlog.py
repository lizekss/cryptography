import math


# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(p, g, h, max_x):
	B = int(math.sqrt(max_x))
	table = dict()
	inv = pow(g, p - 2, p)
	div = 1
	for x_1 in range(B + 1):
		val = (h * div) % p
		table[val] = x_1
		div = (div * inv) % p
	for x_0 in range(B + 1):
		rhs = pow(g, B * x_0, p)
		if rhs in table:
			x_1 = table[rhs]
			x = x_0 * B + x_1
			return x
	return -1

def main():
	p = int(input().strip())
	g = int(input().strip())
	h = int(input().strip())
	max_x = 1 << 40 # 2^40

	dlog = discrete_log(p, g, h, max_x)
	print(dlog)


if __name__ == '__main__':
	main()
