problems = [6]

def fact(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

def C(n, k):
    return fact(n) // fact(k) // fact(n - k)

def v(n, p):
    val = 0
    while n % p == 0:
        n //= p
        val += 1
    return val

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def harmonic_mod(u, p):
    ans = 0
    for i in range(1, u + 1):
        ans += modinv(i, p)
    return ans % p


# begin problem 3
if 3 in problems:
    for p in [7,11,13,17,19,23,29]:
        print (p, (fact(p-1) // (p + 1) + 1) // p)

# end problem 3


# problem 4 (just in case)
if 4 in problems:
    print (pow(2021, 2020, 1000))
    print (pow(2021, pow(2020, 2019), 1000))
    print (pow(21, 20, 1000))
    print (pow(2020, 2019, 400))
# end problem 4

# begin problem 6
def base(n, p):
    out = [0,0]
    out[1] = n % p
    n //= p
    out[0] = n % p
    return out

def g(p):
    ans = 0
    mod = pow(p, 2)
    for i in range(1, p):
        ans = (ans + pow(i, p, mod)) % (mod)
    return ans

for p in [5, 7, 11, 13, 17, 19, 23]:
    for i in range(1, p):
        # break
        # x = pow(i, 2*p-1, p**2)
        # digits = base(x, p)
        # print (i, x, *digits)
        # print (i, pow(i, 2*p, p**2))
        # print (i, pow(i, p, p**2))
        print (i, modinv(i, p**2))
    # print (p, g(p))
    print ()

# end problem 6

# begin problem 7
if 7 in problems:
    for p in [3,5,7,11,13]:
        # n = C(p*p, p) - p
        # s = v(n, p)
        # print (p, s)
        # print (p, harmonic_mod(p - 1, p*p))
        print (p)
        for i in range(1, p):
            print (i, modinv(i, p), modinv(i, p*p))
        print ()
# end problem 7

# begin problem 8
if 8 in problems:
    r = 2
    m = pow(10, 2**r) + 1
    print (pow(10, m - 1, m))
# end problem 8

# begin problem 9
def check(n):
    for d in range(1, n):
        if gcd(n, d) > 1: 
            continue
        if pow(d, 2, n) != 1:
            return False
    return True

if 9 in problems:
    for n in range(2, 10**4):
        if check(n):
            print (n)

# end problem 9


# begin problem 10
def f(n):
    return (n**3 + 5 * n + 6) // 6

if 10 in problems:
    for n in range(3, 10**7):
        i = f(n)
        if not i&(i-1):
            print (n, i)

# end problem 10

