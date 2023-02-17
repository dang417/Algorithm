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
rings = list(map(int, input().split()))

for i in range(1, n):
    print(f'{rings[0]//gcd(rings[0], rings[i])}/{rings[i]//gcd(rings[0], rings[i])}')