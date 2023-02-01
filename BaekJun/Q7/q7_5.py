t = int(input())
for k in range(1,t+1):
    count = 0
    H, W, N = map(int,input().split())
    for i in range(1,W+1):
        for j in range(1,H+1):
            count += 1
            if count == N:
                if i >= 10:
                    print(f'{j}{i}')
                else :
                    print(f'{j}0{i}')
                
