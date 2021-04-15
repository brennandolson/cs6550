from collections import defaultdict as dd
from bisect import bisect as bis, bisect_left as bis2
from time import time

def rl():
    return list(map(int, input().split()))



n, k = rl()
A = [0] * n

for i in range(k):
    c, l, r, v = rl()
    if c == 1:
        for j in range(l, r + 1):
            A[j] = min(A[j], v)
    else:
        for j in range(l, r + 1):
            A[j] = max(A[j], v)
print (*A)
# print (time() - start)

# A = [0] * 10
# T = Tree(A)
# 
# T.maximize(1, 8, 4)
# T.final()
# T.minimize(4, 9, 1)
# T.final()
# T.minimize(3, 6, 5)
# T.final()
# T.maximize(0, 5, 3)
# T.final()
# T.maximize(2, 2, 5)
# T.final()
# T.minimize(6, 7, 0)
# T.final()
# T.debug()
