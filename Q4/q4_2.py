n , x = map(int,input().split())
a = list(map(int,input().split()))
sol = []
for i in range(0,n) :
    if a[i] < x :
        sol.append(a[i])

a = ' '.join(str(s) for s in sol)

print(a)