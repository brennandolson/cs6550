from collections import defaultdict as dd
from bisect import bisect as bis, bisect_left as bis2

INF = 10**10
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.opmin = INF
        self.opmax = -INF
        if (self.start == self.end):
            self.left = None
            self.right = None
        else:
            m = (self.start + self.end) // 2
            self.left = Node(self.start, m)
            self.right = Node(m + 1, self.end)
        self.last_update = -1

    def minimize(self, l, r, t, timestamp):
        if (self.start == l and self.end == r):
            self.last_update = timestamp
            self.opmin = min(self.opmin, t)
            self.opmax = min(self.opmin, self.opmax)
        else:
            self.left.minimize(self.left.start, self.left.end, self.opmin, timestamp)
            self.left.maximize(self.left.start, self.left.end, self.opmax, timestamp)
            self.right.minimize(self.right.start, self.right.end, self.opmin, timestamp)
            self.right.maximize(self.right.start, self.right.end, self.opmax, timestamp)
            if (r <= self.left.end):
                self.left.minimize(l, r, t, timestamp)
            elif (l >= self.right.start):
                self.right.minimize(l, r, t, timestamp)
            else:
                self.left.minimize(l, self.left.end, t, timestamp)
                self.right.minimize(self.right.start, r, t, timestamp)

    def maximize(self, l, r, t, timestamp):
        if (self.start == l and self.end == r):
            self.last_update = timestamp
            self.opmax = max(self.opmax, t)
            self.opmin = max(self.opmin, self.opmax)
        else:
            self.left.minimize(self.left.start, self.left.end, self.opmin,timestamp)
            self.left.maximize(self.left.start, self.left.end, self.opmax,timestamp)
            self.right.minimize(self.right.start, self.right.end, self.opmin,timestamp)
            self.right.maximize(self.right.start, self.right.end, self.opmax,timestamp)
            if (r <= self.left.end):
                self.left.maximize(l, r, t, timestamp)
            elif (l >= self.right.start):
                self.right.maximize(l, r, t, timestamp)
            else:
                self.left.maximize(l, self.left.end, t, timestamp)
                self.right.maximize(self.right.start, r, t, timestamp)


    def propogate(self, A, lo, hi, recency):
        if self.last_update < recency:
            self.opmin = min(self.opmin, lo)
            self.opmax = max(self.opmax, hi)
        else:
            recency = self.last_update
        if self.start == self.end:
            i = self.start
            v = min(self.opmin, A[i])
            v = max(self.opmax, v)
            A[i] = v
        else:
            self.left.propogate(A, self.opmin, self.opmax, recency)
            self.right.propogate(A, self.opmin, self.opmax, recency)

    def debug(self):
        print ("[{}, {}]: min={}, max={}".format(self.start, self.end, self.opmin, self.opmax))
        print ("last update: {}".format(self.last_update))
        if self.start < self.end:
            self.left.debug()
            self.right.debug()
        
class Tree:
    def __init__(self, A):
        self.n = len(A)
        self.root = Node(0, self.n - 1)
        self.A = A
        self.clock = 0

    def minimize(self, l, r, t):
        self.root.minimize(l, r, t, self.clock)
        self.clock += 1

    def maximize(self, l, r, t):
        self.root.maximize(l, r, t, self.clock)
        self.clock += 1

    def final(self):
        self.root.propogate(self.A, INF, -INF, -1)
        print (self.A)

    def debug(self):
        self.root.debug()

A = [0] * 10
T = Tree(A)

T.maximize(1, 8, 4)
T.minimize(4, 9, 1)
T.final()
T.debug()
