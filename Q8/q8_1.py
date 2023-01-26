#숫자의 약수가 1과 자기자신 밖에 없을 때
t = int(input())
num = list(map(int,input().split()))

for i in num:
    for j in range(1,i+1):
        if i == 1:
            t -=1
        elif i % j == 0 and i != j and j != 1:
            t -= 1
            break
print(t)