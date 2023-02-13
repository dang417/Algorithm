a, b = map(int, input().split())
if b > a:
    a, b = b, a

while True:
    x, y = a, b
    gcd = x % y
    x = x // y
    if y % gcd == 0:
        break
    x, y = y, x

x = a // gcd
y = b // gcd

lcm = x * y * gcd

print(gcd)
print(lcm)