def ri():
    return int(input())

def rl():
    return list(map(float, input().split()))



n = ri()
A = rl()
A.sort()

eps = 10**-7
def check(x, a):
    b = int(round(a / x))
    if (a * 0.99 <= x * b + eps) and (a * 1.01 >= x * b - eps):
        return True
    else:
        return False

def fix(x, a):
    # want x*b = 1.01*a
    # with x as large as possible
    b = int(a/x + 1) # don't need epsilon if already failed check 
    return (a * 1.01) / b


x = 1.01 * A[0]
done = False
while not done:
    done = True
    for a in A:
        if not check(x, a):
            x = fix(x, a)
            done = False
    # print (x)
    # input()

print ("{:.4f}".format(x))
