t = int(input())

for tc in range(1, t+1):
    n = int(input())
    clothes = {}
    rlt = 1
    for i in range(n):
        a, b = input().split()
        if b in clothes:
            clothes[b] += [a]
        else:
            clothes[b] = [a]

    
    for i in clothes:
        rlt *= len(clothes[i])+1
    print(rlt-1)