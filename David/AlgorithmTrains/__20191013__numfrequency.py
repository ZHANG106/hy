M, N, X = list(map(int, input().split(" ")))

count = 0
for i in range(M,N+1):
    for j in str(i):

        if str(X) == j :
            count +=1

print(count)
