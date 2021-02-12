# sieving for totient values
N = 5 * 10**6
phi = list(range(N + 1))
primes = set()
for p in range(2, N + 1):
    if phi[p] == p:
        primes.add(p)
        for q in range(p, N + 1, p):
            phi[q] //= p
            phi[q] *= (p - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def order(a, n):
    o = 1
    f = a
    while (a != 1):
        a = (a * f) % n
        o += 1
    return o

# N = 7 * 33
# for i in range(1, N):
    # if gcd(i, N) == 1:
        # print (i, order(i, N))

# for p in [5,7,11,13,17,19,23]:
    # x = (pow(2, 2*p) - 1) // 3
    # print (p, x, phi[x], order(2, x))
    # print (p, x, order(2, x))
    print (p, x, pow(2, x - 1, x))

# for n in range(2, 11):
    # x = (pow(2, 2 * n) - 1) // 3
    # print (n, order(2, x))

def pseudoprime(n, b):
    return pow(b, n - 1, n) == 1

P = [2,3,5,7,11,13,17,19,23,29,31]

for i in range(1, 10**6):
    if i not in primes and all([pseudoprime(i, b) for b in P]):
        print (i)   
