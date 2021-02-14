from collections import defaultdict as dd
from bisect import bisect as bis, bisect_left as bis2

mod = 998244353
N = 1<<20
ti = 998243401 # (2^{-20} % mod)

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))

def digsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

def get_valid(L):
    masks = [0] * N
    n = len(L)
    cutoff = (n + 1) >> 1
    counts = [0] * 5
    xors   = [0] * 5
    
    def backtrack(i):
        if i == n:
            if max(counts) >= cutoff:
                mask = 0
                shift = 1
                for j in range(5):
                    mask += xors[j] * shift
                    shift <<= 4
                masks[mask] += 1
        else:
            for j in range(5):
                counts[j] += 1
                xors[j] ^= L[i]
                backtrack(i + 1)
                counts[j] -= 1
                xors[j] ^= L[i]

    backtrack(0)
    return masks

def fwht(a):
    """In-place Fast Walsh–Hadamard Transform of array a."""
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x = a[j]
                y = a[j + h]
                # a[j] = (x + y) % mod
                # a[j + h] = (x - y) % mod
                a[j] = x + y
                a[j + h] = x - y
        h *= 2
    # for i in range(n):
        # a[i] %= mod



# main 
# pre-processing
n, q = rl()
ghosts = []
for _ in range(n):
    bitset = 0
    moves = set(input().split()[1:])
    if "spook" in moves:
        bitset |= 1
    if "hide" in moves:
        bitset |= 2
    if "creep" in moves:
        bitset |= 4
    if "float" in moves:
        bitset |= 8
    ghosts.append(bitset)
scores = rl()    
def get_score(m):
    total_score = 0
    i = 0
    while m:
        total_score += scores[i] * (m&1)
        m >>= 1
        i = (i + 1) % 4
    return total_score
    
# brute force combinatorics (backtracking)
groups = dd(list)
for i in range(n):
    groups[digsum(i+1)].append(ghosts[i])
masks = [get_valid(L) for L in groups.values()]


# using walsh-hadamard in place
# storing final result in first
# array. Not using sqrt(2), so 
# in the end, need to back out
# 2^20 (mod p)
for i in range(len(masks)):
    fwht(masks[i])

for i in range(1, len(masks)):
    for j in range(N):
        masks[0][j] = (masks[0][j] * masks[i][j]) % mod

fwht(masks[0])
for i in range(N):
    masks[0][i] = (masks[0][i] * ti) % mod


# filling sparse array of counts
# of possible scores
ways = dd(int)
for i in range(N):
    v = masks[0][i]
    if v != 0:
        ways[get_score(i)] += v

S = sorted(list(ways.keys()))
m = len(S)
partials = [0] * (m + 1)
for i in range(m):
    partials[i + 1] = partials[i] + ways[S[i]]

# process queries
for _ in range(q):
    a, b = rl()
    i = bis(S, a - 1)
    j = bis(S, b)
    print ((partials[j] - partials[i]) % mod)
