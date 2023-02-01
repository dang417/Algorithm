a = list(map(int,input().split()))
b = [1,1,2,2,2,8]
for i in range(len(a)) :
    print(b[i] - a[i], end=' ')