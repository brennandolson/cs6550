from random import random as rand
n = int(input())
print (n, 3)

for i in range(n):
    fail = True
    while fail:
        amt = 0
        moves = []
        for move in ["spook", "hide", "creep", "float"]:
            if rand() < 0.5:
                amt += 1
                moves.append(move)
                fail = False
    print (amt, *moves)

print (125344, 2693, 1000000000, 7)
print (1, 1000000000)
print (1, 100000000)
print (100000000, 1000000000)
