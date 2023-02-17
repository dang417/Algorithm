n, k = map(int, input().split())
a = 1
b = 1
for i in range(n-k+1, n+1):
    a = a * i

for j in range(1, k+1):
    b = b * j

print(a//b)