M = int(input())

def getnum(n):

    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return getnum(n - 1) + getnum(n - 2)

print(getnum(M))

