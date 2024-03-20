from oracle import *
from helper import *

def inv(a, N):
  return pow(a, -1, N)

def get_signature(m, N):
  # Sign(x) = (x * 2^512 + x)^d = x^d * (2^512 + 1)^d
  # y = 2^512 + 1
  # Sign(x) = x^d * y^d
  # Sign(1) = 1^d * y^d = y^d
  # Sign(2m) = 2^d * m^d * y^d
  # Sign(2) = 2^d * y^d
  # Sign(m) = m^d * y^d = Sign(2m) * Sign(1) / Sign(2)
  # We can do a similar thing for divisors of m, since we technically were not allowed to go over 63 bytes
  # Sign(m) = Sign(div) * Sign(m/div) / Sign(1)
  # But this works and it doesn't require looping so I'm leaving it this way
  return (Sign(2*m) * Sign(1) * inv(Sign(2), N)) % N

def main():
  with open('project_3_2/input.txt', 'r') as f:
    n = int(f.readline().strip())
    msg = f.readline().strip()

  Oracle_Connect()    

  m = ascii_to_int(msg)
  sigma = get_signature(m, n) 

  print(sigma)
  # print(Verify(m, sigma))
  # if Verify(m, sigma):
  #   print('Passed!')

  Oracle_Disconnect()

if __name__ == '__main__':
  main()
