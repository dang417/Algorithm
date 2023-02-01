t = int(input())

for test in range(t):
    black = input()
    *pancake,d = map(int,input().split())
    pancake = sorted(pancake)
    s = sum(pancake)-d
    tmp = min(s//3,pancake[0])
    a = tmp
    s -= tmp
    tmp = min(s//2,pancake[1])
    print(a*tmp*(s-tmp))
