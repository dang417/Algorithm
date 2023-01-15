n = int(input())
a = n // 10
b = n % 10
c = a + b
t = 1
while 10 * b + c != n :
    a = b
    b = c
    c = (a+b) % 10
    t = t + 1
print(t)
