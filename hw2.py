# problem 12
def pythagoras(n):
    ans = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if (x**2 + y**2 - z**2) % n == 0:
                    ans += 1
    return ans

for n in range(1, 20):
    print (n, pythagoras(n))

print ()
for p in [2, 3, 5, 7, 11, 13, 17]:
    check = 0
    for x in range(p):
        for y in range(p):
            if (x**2 + y**2) % p == 1:
                check += 1
    print (p, check)

# problem 11
# def isqrt(n):
#     i = int(n**0.5)
#     while (i+1)**2 <= n:
#         i += 1
#     return i
# 
# def is_square(n):
#     i = isqrt(n)
#     return n == i*i
# 
# 
# def rwh_primes(n):
#     # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
#     """ Returns  a list of primes < n """
#     sieve = [True] * n
#     for i in range(3,int(n**0.5)+1,2):
#         if sieve[i]:
#             sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
#     return [2] + [i for i in range(3,n,2) if sieve[i]]
# 
# P = rwh_primes(10**6)
# N = 10000
# for p in P:
#     p3 = p**3
#     for x in range(p + 1, p + N):
#         y2 = x**3 - p3
#         if is_square(y2):
#             y = isqrt(y2)
#             # if y % 3 == 0 or y % x == 0:
#             if y % 3 == 0 or y % p == 0:
#                 continue
#             print (p, x, y)

# problem 5
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# N = 10**3
# M = 20
# for x in range(1, N):
    # for y in range(x, N):
        # for m in range(1, M):
            # for n in range(m + 1, m + M):
                # if pow(x**2+y**2, m) == pow(x*y, n):
                    # print (x, y, m, n)

