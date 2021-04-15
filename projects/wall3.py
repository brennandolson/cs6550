from collections import defaultdict as dd
from bisect import bisect as bis, bisect_left as bis2
from time import time
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def rl():
    return list(map(int, input().split()))



INF = 10**10
class Node:
    def __init__(self, start, end, parent=None):
        self.start = start
        self.end = end
        self.opmin = INF
        self.opmax = -INF
        self.parent = parent
        if (self.start == self.end):
            self.left = None
            self.right = None
        else:
            m = (self.start + self.end) // 2
            self.left = Node(self.start, m, self)
            self.right = Node(m + 1, self.end, self)

    def minimize(self, l, r, t):
        if (self.start == l and self.end == r):
            self.opmin = min(self.opmin, t)
            self.opmax = min(self.opmin, self.opmax)
        else:
            self.left.minimize(self.left.start, self.left.end, self.opmin)
            self.left.maximize(self.left.start, self.left.end, self.opmax)
            self.right.minimize(self.right.start, self.right.end, self.opmin)
            self.right.maximize(self.right.start, self.right.end, self.opmax)
            self.opmin = INF
            self.opmax = -INF
            if (r <= self.left.end):
                self.left.minimize(l, r, t)
            elif (l >= self.right.start):
                self.right.minimize(l, r, t)
            else:
                self.left.minimize(l, self.left.end, t)
                self.right.minimize(self.right.start, r, t)

    def maximize(self, l, r, t):
        if (self.start == l and self.end == r):
            self.opmax = max(self.opmax, t)
            self.opmin = max(self.opmin, self.opmax)
        else:
            self.left.minimize(self.left.start, self.left.end, self.opmin)
            self.left.maximize(self.left.start, self.left.end, self.opmax)
            self.right.minimize(self.right.start, self.right.end, self.opmin)
            self.right.maximize(self.right.start, self.right.end, self.opmax)
            self.opmin = INF
            self.opmax = -INF
            if (r <= self.left.end):
                self.left.maximize(l, r, t)
            elif (l >= self.right.start):
                self.right.maximize(l, r, t)
            else:
                self.left.maximize(l, self.left.end, t)
                self.right.maximize(self.right.start, r, t)

    def query(self):
        cmin = self.opmin
        cmax = self.opmax
        node = self
        while node.parent:
            node = node.parent
            cmin = min(cmin, node.opmin)
            cmax = min(cmin, cmax)
            cmax = max(cmax, node.opmax)
            cmin = max(cmin, cmax)
        return max(0, cmax)

    def propogate(self, A):
        if self.start == self.end:
            A[self.start] = self.query()
        else:
            self.left.propogate(A)
            self.right.propogate(A)
   
    def debug(self):
        print ("[{}, {}]: min={}, max={}".format(self.start, self.end, self.opmin, self.opmax))
        if self.start < self.end:
            self.left.debug()
            self.right.debug()
        
class Tree:
    def __init__(self, A):
        self.n = len(A)
        self.root = Node(0, self.n - 1)
        self.A = A

    def minimize(self, l, r, t):
        self.root.minimize(l, r, t)

    def maximize(self, l, r, t):
        self.root.maximize(l, r, t)

    def final(self):
        self.root.propogate(self.A)
        # print (*self.A)
        for a in self.A:
            print (a)

    def debug(self):
        self.root.debug()

# start = time()
n, k = rl()
A = [0] * n
T = Tree(A)

for i in range(k):
    c, l, r, v = rl()
    if c == 2:
        T.minimize(l, r, v)
    else:
        T.maximize(l, r, v)
T.final()

# print (time() - start)
