from math import pi

# problem 1
def solve(x):
    return 12 * 60 * 60 * x / 11

def s_to_time(t):
    '''
    converts t, a time in seconds with
    0 <= t < 43200 into hh:mm:ss format
    '''
    t = int(t)
    s = t % 60
    t = (t - s) // 60
    m = t % 60
    h = t // 60
    h = h + 12 if not h else h
    return "{:02d}:{:02d}:{:02d}".format(h, m, s)

for a in range(24):
    t = solve(a + 1/(2*pi))
    if 0 <= t < 43200:
        print ("'" + s_to_time(t))
    t = solve(a + 1 - 1/(2*pi))
    if 0 <= t < 43200:
        print ("'" + s_to_time(t))


# problem 6
A = []
for x in range(60):
    if x == x // 2 + x // 3 + x // 5:
        A.append(x)
print (A)

# thinking about problem 8
S = set()
for a in range(-10, 11):
    for b in range(-10, 11):
        S.add(a*a + b*b - a * b)

for x in sorted(S):
    print (x)

# thinking about problem 9
def alternating(n):
    d = []
    while n:
        d.append(n % 10)
        n //= 10
    for i in range(len(d) - 1):
        if (d[i] ^ d[i+1]) & 1:
            continue
        else:
            return False
    return True

def first_alternating(n):
    orig = n
    while not alternating(n):
        n += orig
    return n

# for i in range(1, 100):
    # if i % 20 == 0:
        # continue
    # print (i, first_alternating(i))

for p in range(1, 6):
    power_2 = 2**p
    lo = (10**(p-1) // power_2) * power_2
    hi = 10**p
    print (power_2)
    for n in range(lo, hi, power_2):
        if n < 10**(p-1):continue
        if alternating(n):
            print ("  ", n)
    # else:
        # print (power_2, "not found")
quit()



x = 5
pp = 25
parity = 0
p10 = 10
print (x)
for _ in range(10):
    for d in range(0, 10, 2):
        if (p10 * (d + parity) + x) % pp == 0:
            x += p10 * (d + parity)
            break
    else:
        print ('unable to continue pattern')
    pp *= 5
    p10 *= 10
    parity ^= 1
    print (x)

quit()
# thinking about problem 10
A = [0,1,2]
l = 0.4
for i in range(1000):
    A[0] = A[-1] + l * (A[-1] - A[0])
    A.sort()
    print (A)


A = [0, 1, 2]
l = 0.5

while 1:
    print (A)
    inp = input()
    if not len(inp):
        break
    i, j = map(int, inp.split())
    for _ in range(1000):
        if A[j] < A[i]:
            i, j = j, i
        A[i], A[j] = A[j], A[j] + l * (A[j] - A[i])


