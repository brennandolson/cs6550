n = int(input())
scores = [100,100]
for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        scores[0] -= b
    elif a > b:
        scores[1] -= a
print (scores[0])
print (scores[1])
