from collections import defaultdict as dd
from bisect import bisect as bis, bisect_left as bis2

INF = 10**10
class Node:
    def __init__(self, start, end, parent=None):
        self.start = start
        self.end = end
        self.opmin = INF
        self.opmax = -INF
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

    def query(
   
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
        print (self.A)

    def debug(self):
        self.root.debug()

A = [0] * 4
T = Tree(A)

T.maximize(0, 3, 4)
T.minimize(1, 3, 1)
# T.final()
T.debug()
