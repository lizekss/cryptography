from core import repeating_encrypt

k = input().strip()
m = input().strip()

c = repeating_encrypt(k, m)

print(c)