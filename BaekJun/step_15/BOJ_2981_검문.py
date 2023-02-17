def gcd(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

n = int(input())
m = sorted([int(input()) for _ in range(n)])
o = []

for i in range(1, n):
    o.append(m[i]-m[i-1])

g = o[0]
for i in range(1, len(o)):
    g = gcd(g, o[i])

rlt = set()
for i in range(2, int(g**0.5) + 1):
    if g % i == 0:
        rlt.add(i)
        rlt.add(g // i)

rlt.add(g)
print(*sorted(list(rlt)))